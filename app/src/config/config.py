"""Configuration file.

Configuration of project variables that we want to have available
everywhere and considered configuration.
"""
import os
from dataclasses import dataclass
from maikol_utils.file_utils import make_dirs

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

    output_model_dir: str = os.path.join(MODELS_PATH, "es_to_eo_finetuned")
    logging_dir: str = os.path.join(RESULTS_PATH, "logs")

    # =========================== PARAMETERS ===========================
    val_split: float = 0.15
    test_split: float = 0.15

    model_name: str = ""
    fine_tune_model_name: str = "finetuned-es-to-eo"
    src_name: str = "Spanish"
    tgt_name: str = "Esperanto"
    src_code: str = "spa_Latn"
    tgt_code: str = "epo_Latn"

    max_tok_length: int = 16
    batch_size: int = 32
    max_batches: int = 1000

    def __post_init__(self):
        self.fine_tune_model_name = f"{self.model_name.split('/')[-1]}-finetuned-es-to-eo"
        self.output_dir = os.path.join(self.MODELS_PATH, self.fine_tune_model_name)
        self.logging_dir = os.path.join(self.output_dir, "logs")
        make_dirs([
            self.DATA_PATH,
            self.RAW_DATA_PATH,
            self.PROCESSED_DATA_PATH,
            self.MODELS_PATH,
            self.RESULTS_PATH
        ])

    