"""Configuration file.

Configuration of project variables that we want to have available
everywhere and considered configuration.
"""
import os
from dataclasses import dataclass


@dataclass
class Configuration:
    DATA_PATH: str = os.path.join("..", "data")
    RAW_DATA_PATH: str = os.path.join(DATA_PATH, "raw")
    PROCESSED_DATA_PATH: str = os.path.join(DATA_PATH, "processed")
    MODELS_PATH: str = os.path.join("..", "models")
    RESULTS_PATH: str = os.path.join("..", "results")

    spanish_data: str = os.path.join(RAW_DATA_PATH, "CCMatrix.eo-es.es")
    esperanto_data: str = os.path.join(RAW_DATA_PATH, "CCMatrix.eo-es.eo")

    corpus_path: str = os.path.join(PROCESSED_DATA_PATH, "corpus.csv")
    corpus_raw_path: str = os.path.join(PROCESSED_DATA_PATH, "corpus_raw.csv")

    # =========================== PARAMETERS ===========================
    val_split: float = 0.15
    test_split: float = 0.15

    model_name: str = ""
    src_name: str = "Spanish"
    tgt_name: str = "Esperanto"
    src_code: str = "spa_Latn"
    tgt_code: str = "epo_Latn"

    max_tok_length: int = 16

    max_batches: int = 1000
