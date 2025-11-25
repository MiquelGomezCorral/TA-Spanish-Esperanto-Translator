# TA-Spanish-Esperanto-Translator
A project for my master course 'Traducción Automática'. This project is about the usage and creations / train / fine-tune of models for translation from Spanish to Esperanto.

### Project paper
This [paper](https://github.com/MiquelGomezCorral/TA-Spanish-Esperanto-Translator-Paper) has been written for the results and deliver of the project.

# Dataset source
- [CCMatrix](https://opus.nlpl.eu/CCMatrix/corpus/version/CCMatrix), a crawled dataset with pair of samples from +100 languages.


# User project
- Create local env
```bash
 python3.12 -m venv venv
 source venv/bin/activate
 
 # install module
 pip install -e app/
 
 # install requirements
 pip install uv
 uv pip install -r requirements.txt

 pip install ipykernel
 python -m ipykernel install --user --name=venv --display-name "Python (venv)"

```

# Structure
```
.
├── app
│   ├── main.py
│   ├── setup.py
│   └── src
│       ├── config          <- Project configuration class
│       ├── data            <- Dataset wrapper
│       └── utils
├── data
│   ├── processed
│   │   ├── corpus.csv
│   │   └── corpus_raw.csv
│   └── raw
│       ├── CCMatrix.eo-es.eo
│       ├── CCMatrix.eo-es.es
│       ├── CCMatrix.eo-es.scores
│       └── eo-es.txt.zip
├── docs
│   └── A2_Coursework_neural_models.pdf
├── example.env
├── models
│   ├── Trained models...
├── notebooks
│   ├── ES-EO-L3.4_NMT_mt5-large_Baseline.ipynb
│   ├── ES-EO-L3.4_NMT_mt5-large_Finetuning-bleu-base.ipynb
│   ├── ES-EO-L3.4_NMT_mt5-large_Finetuning-chrf-base.ipynb
│   ├── ES-EO-L3.4_NMT_mt5-large_Finetuning-chrf-inference.ipynb
│   ├── ES-EO-L3.4_NMT_NLLB_Finetuning.ipynb
│   ├── ES-EO-L3.5_NMT_LLAMA-3_Prompting.ipynb
│   ├── ES-EO-L3.5_NMT_LLAMA_Finetuning.ipynb
│   ├── ES-EO-L3.5_NMT_LLAMA_Prompting.ipynb
│   ├── ES-EO-LL3.4_NMT_NLLB_Baseline.ipynb
│   ├── L3.4_NMT_NLLB_Baseline.ipynb
│   ├── L3.4_NMT_NLLB_Finetuning.ipynb
│   ├── L3.5_NMT_LLAMA_Finetuning.ipynb
│   ├── L3.5_NMT_LLAMA_Prompting.ipynb
│   └── Process-dataset.ipynb
├── README.md
├── requirements.txt
├── scripts
│   └── run_notebooks.sh
```