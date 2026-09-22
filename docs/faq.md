# FAQ — Placeholder

**Q: Where does data come from?**
A: UCI ML Repository, fetched at runtime. See `data/README.md` and `config/config.yaml`.

**Q: Why both R and Python?**
A: Project keeps pipelines in sync for reproducibility cross-check.

**Q: How to reproduce?**
A: `make all` or `bash run_analysis.sh` or `docker build -t wine-analysis . && docker run ...`.

**Q: Figures not showing?**
A: Ensure `output/` and `figures/` were generated. Check CI artifacts.

> TODO: Expand with troubleshooting placeholders.

