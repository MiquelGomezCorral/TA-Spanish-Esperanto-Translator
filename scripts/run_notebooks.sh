#!/bin/bash

# Exit on error
set -e

echo "Starting notebook execution..."

echo "Running ES-EO-L3.5_NMT_LLAMA_Prompting.ipynb..."
jupyter nbconvert --to notebook --execute --inplace notebooks/ES-EO-L3.5_NMT_LLAMA_Prompting.ipynb

echo "Running ES-EO-L3.5_NMT_LLAMA-3_Prompting.ipynb..."
jupyter nbconvert --to notebook --execute --inplace "notebooks/ES-EO-L3.5_NMT_LLAMA-3_Prompting.ipynb"

echo "Running ES-EO-L3.4_NMT_ mt5-large _Finetuning.ipynb..."
jupyter nbconvert --to notebook --execute --inplace "notebooks/ES-EO-L3.4_NMT_ mt5-large _Finetuning.ipynb"

echo "Running ES-EO-L3.5_NMT_LLAMA_Finetuning.ipynb..."
jupyter nbconvert --to notebook --execute --inplace notebooks/ES-EO-L3.5_NMT_LLAMA_Finetuning.ipynb

echo "All notebooks executed successfully!"