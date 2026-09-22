# helpers.R — Placeholder for shared R utilities
# TODO: Fill with reusable functions as project grows.

# Example stub: project root helper
get_project_root <- function() {
  if (file.exists("scripts/Wine_Quality_Analysis.R")) return(".")
  if (file.exists("../scripts/Wine_Quality_Analysis.R")) return("..")
  return(".")
}

# Example stub: save wrapper
save_plot <- function(plot, filename, width=8, height=6) {
  outdir <- file.path(get_project_root(), "output")
  if (!dir.exists(outdir)) dir.create(outdir, recursive=TRUE)
  ggsave(file.path(outdir, filename), plot=plot, width=width, height=height, dpi=150)
}

# TODO: add theme_wine(), compute_metrics(), etc.
