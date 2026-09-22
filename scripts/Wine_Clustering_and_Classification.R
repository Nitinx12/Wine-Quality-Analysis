# =================================================================================
# Wine_Clustering_and_Classification.R
#
# A complementary R script to perform clustering and supervised learning on
# the UCI Wine Quality datasets (red & white).
#
# Features:
#   1. Downloads & prepares red & white wine CSVs
#   2. K-means clustering on standardized chemical attributes
#       • Elbow & silhouette analysis to choose k
#       • PCA scatter with cluster assignments
#   3. Binary classification of "high" vs "low" quality wines
#       • Logistic regression
#       • Random forest
#       • Cross-validation & hyperparameter tuning
#       • Confusion matrices & ROC curves
#
# Dependencies:
#   - tidyverse
#   - cluster
#   - factoextra
#   - caret
#   - randomForest
#   - pROC
#
# Usage:
#   1. Ensure R >= 4.0 is installed.
#   2. Run: Rscript scripts/Wine_Clustering_and_Classification.R
#   3. Or via Makefile: make clustering
# =================================================================================

# 0. Install & load packages (non-interactive safe)
pkgs <- c(
  "tidyverse", "cluster", "factoextra",
  "caret", "randomForest", "pROC"
)
for(pkg in pkgs) {
  if(!requireNamespace(pkg, quietly=TRUE)) install.packages(pkg, repos="https://cloud.r-project.org")
  library(pkg, character.only=TRUE)
}

# 0b. Resolve project root & ensure output dir exists (works from repo root or scripts/)
if (file.exists("scripts/Wine_Clustering_and_Classification.R")) {
  project_root <- "."
} else if (file.exists("../scripts/Wine_Clustering_and_Classification.R")) {
  project_root <- ".."
} else {
  project_root <- "."
}
outdir <- file.path(project_root, "output")
if(!dir.exists(outdir)) dir.create(outdir, recursive=TRUE)
set.seed(123)

# 1. URLs & read data
url_red   <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
url_white <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

spec <- cols(.default = col_double(),
             quality = col_integer())

red   <- read_delim(url_red,   delim=";", col_types=spec) %>% mutate(type="red")
white <- read_delim(url_white, delim=";", col_types=spec) %>% mutate(type="white")

wine <- bind_rows(red, white) %>%
  mutate(type = factor(type))

# 2. Prepare for clustering: numeric attributes only (exclude quality + type)
nums <- wine %>%
  select(-type, -quality)

# Standardize
nums_scaled <- scale(nums)

# 3. K-means clustering: Elbow method (saved, not just displayed)
p_elbow <- fviz_nbclust(nums_scaled, kmeans, method="wss", k.max=10) +
  ggtitle("Elbow Method: Optimal Clusters")
print(p_elbow)
ggsave(file.path(outdir, "cluster-elbow.png"), plot=p_elbow, width=8, height=6, dpi=150)

# 4. K-means clustering: Silhouette analysis (saved)
p_sil <- fviz_nbclust(nums_scaled, kmeans, method="silhouette", k.max=10) +
  ggtitle("Silhouette Analysis: Optimal Clusters")
print(p_sil)
ggsave(file.path(outdir, "cluster-silhouette.png"), plot=p_sil, width=8, height=6, dpi=150)

# Choose k = 3 (for example)
set.seed(123)
km_res <- kmeans(nums_scaled, centers=3, nstart=25)

# 5. Visualize clusters on first 2 PCs (saved)
pca_res <- prcomp(nums_scaled, center=TRUE, scale.=FALSE)
p_pca <- fviz_pca_ind(pca_res,
             geom.ind="point",
             col.ind=as.factor(km_res$cluster),
             palette="jco",
             addEllipses=TRUE,
             legend.title="Cluster") +
  ggtitle("PCA Scatter: K-means Clusters")
print(p_pca)
ggsave(file.path(outdir, "cluster-pca.png"), plot=p_pca, width=8, height=6, dpi=150)

# 6. Add cluster assignments back to data
wine$cluster <- factor(km_res$cluster)

# 7. Binary classification: define high quality >= 7
wine <- wine %>%
  mutate(high_quality = factor(ifelse(quality >= 7, "yes", "no"), levels=c("no","yes")))

# 8. Train/test split
set.seed(2024)
train_idx <- createDataPartition(wine$high_quality, p=0.7, list=FALSE)
train <- wine[train_idx, ]
test  <- wine[-train_idx, ]

# 9. Logistic regression
glm_fit <- train(
  high_quality ~ alcohol + sulphates + pH + citric.acid + residual.sugar,
  data = train,
  method = "glm",
  family = "binomial",
  trControl = trainControl(method="cv", number=5, classProbs=TRUE, summaryFunction=twoClassSummary),
  metric = "ROC"
)
print(glm_fit)

# 10. Random Forest (exclude leakage vars: cluster was built on full data, so excluded)
rf_fit <- train(
  high_quality ~ . - type - quality - cluster,
  data = train,
  method = "rf",
  trControl = trainControl(method="cv", number=5, classProbs=TRUE, summaryFunction=twoClassSummary),
  metric = "ROC",
  tuneLength = 5
)
print(rf_fit)
print(varImp(rf_fit))

# 11. Evaluate on test set (save ROC plots)
models <- list(Logistic=glm_fit, RandomForest=rf_fit)
for(name in names(models)) {
  cat("\n=== Evaluating", name, "===\n")
  preds <- predict(models[[name]], test, type="prob")[, "yes"]
   roc_obj <- roc(test$high_quality, preds, levels=c("no","yes"))
  cat("AUC:", auc(roc_obj), "\n")
  png(file.path(outdir, paste0("roc-", tolower(name), ".png")), width=800, height=600)
  plot(roc_obj, main=paste(name, "ROC Curve"))
  dev.off()
  
  class_pred <- predict(models[[name]], test)
  print(confusionMatrix(class_pred, test$high_quality, positive="yes"))
}

# =================================================================================
# End of Wine_Clustering_and_Classification.R
# =================================================================================
