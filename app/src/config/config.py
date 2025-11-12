"""Configuration file.

Configuration of project variables that we want to have available
everywhere and considered configuration.
"""
import os
import dataclasses
from dataclasses import dataclass
from argparse import Namespace


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



def args_to_config(args: Namespace):
    """From the args namespace, create a Configuration.

    It will change all the fields that have ben added to the args.
    If a field is not added in the args will be ignored.
    Fields in the args that are not in the Config this will be ignored.

    Args:
        args (Namespace): Parsed arguments. 

    Returns:
        Configuration: Configuration with args values.
    """
    fields = {f.name for f in dataclasses.fields(Configuration)}
    filtered = {k: v for k, v in vars(args).items() if k in fields}
    return Configuration(**filtered)