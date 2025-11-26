# Blinkit Dashboard Project

This repository now includes a project scaffold for the Blinkit dashboard work.

Overview
- Project name: blinkit_dashboard
- Purpose: Build a dashboard for the BlinkIT grocery dataset to explore sales, inventory, and customer behavior.

Files recommended
- blinkit_dashboard.md — this project scaffold and next steps.
- data/BlinkIT Grocery Data cc (1).xlsx — placeholder dataset file. Replace with the real dataset XLSX file when available.

Goals
- Prepare and clean the BlinkIT grocery dataset.
- Build ETL pipelines to ingest and transform data for analysis.
- Create visualizations: top-selling items, category trends, regional sales, inventory alerts.
- Deploy dashboard (Streamlit / Dash / Next.js + API) and add GitHub Actions for CI/CD.

Next steps
1. Replace the placeholder dataset file with the actual XLSX dataset in data/ or the repo root.
2. Add preprocessing scripts, e.g. scripts/preprocess.py, to convert XLSX to CSV/parquet and perform basic cleaning.
3. Implement dashboard app under app/ (Streamlit, Dash, or Next.js) and add README with run instructions.
4. Add unit tests and a GitHub Actions workflow for linting and tests (e.g., .github/workflows/ci.yml).
5. Create issues for backlog items; with the project automation enabled, new issues will become cards automatically.

Security & size notes
- If the Excel file contains sensitive data, do NOT commit it to a public repo. Use a private repo or external storage and add an anonymized sample to the repo.
- If the XLSX is large (>50 MB), use Git LFS or external storage.

Maintainer
- @Abhi5028