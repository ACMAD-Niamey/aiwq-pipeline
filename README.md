# aiwq-pipeline
ECMWF AI Weather Quest Data Engineering and Preprocessing Pipeline

This repository builds a reproducible data engineering pipeline for the ECMWF AI Weather Quest.
It downloads ERA5 data, regrids to 1.5°, constructs weekly windows (Days 19–25, 26–32),
computes climatology/anomalies, and pushes preprocessed datasets to Kaggle.

