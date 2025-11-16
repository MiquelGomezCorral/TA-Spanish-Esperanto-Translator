
import pandas as pd
from datasets import Dataset, DatasetDict
from src.config import Configuration

def get_es_eo_dataset(CONFIG: Configuration):
    df_corpus = pd.read_csv(CONFIG.corpus_path)

    # Rename columns to match the expected format
    df_corpus = df_corpus.rename(columns={
        CONFIG.src_name: 'source_text',
        CONFIG.tgt_name: 'dest_text'
    })

    # Use 0 as the language ID for Esperanto
    df_corpus['dest_lang'] = 0

    # ========================= Shuffle and split the data =========================
    df_corpus = df_corpus.sample(
        frac=CONFIG.data_fraction, 
        random_state=CONFIG.seed
    ).reset_index(drop=True)

    n_total = len(df_corpus)
    n_test = int(n_total * CONFIG.test_split) 
    n_valid = int(n_total * CONFIG.valid_split)  

    df_test = df_corpus[:n_test]
    df_valid = df_corpus[n_test:n_test + n_valid]
    df_train = df_corpus[n_test + n_valid:]

    # ========================= Convert to HuggingFace Dataset format =========================
    raw_datasets = DatasetDict({
        'train': Dataset.from_pandas(df_train[['source_text', 'dest_text', 'dest_lang']]),
        'test': Dataset.from_pandas(df_test[['source_text', 'dest_text', 'dest_lang']]),
        'valid': Dataset.from_pandas(df_valid[['source_text', 'dest_text', 'dest_lang']])
    })

    return raw_datasets