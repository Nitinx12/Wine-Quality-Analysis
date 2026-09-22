# Use the official R image as base (updated from 4.2.2)
FROM r-base:4.3.3

# Install system dependencies (R + Python + pandoc for rmarkdown)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxml2-dev libssl-dev libcurl4-openssl-dev \
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev \
    pandoc pandoc-citeproc \
    python3 python3-pip python3-venv curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Python package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Install R packages (including those needed for clustering)
RUN R -e "install.packages(c('tidyverse','corrplot','factoextra','rmarkdown','caret','randomForest','pROC','cluster'), repos='https://cloud.r-project.org')"

# Copy project files
WORKDIR /home/wine_analysis
COPY . .

# Sync Python dependencies via uv (uses pyproject.toml)
RUN /root/.local/bin/uv sync

# Expose output volumes
VOLUME ["/home/wine_analysis/output", "/home/wine_analysis/figures"]

# Default command: run the Makefile default target
CMD ["make", "all"]
