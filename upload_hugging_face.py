import os

from huggingface_hub import create_repo, upload_file

import pandas as pd

ORGANIZATION = "Wikit/"
REPO_NAME = "nlu-covid"
TRAIN_PATH = "train.jsonl"
TEST_PATH = "test.jsonl"


df_train = pd.read_csv("training_dataset.csv")
df_test = pd.read_csv("test_dataset.csv")

df_train.to_json(TRAIN_PATH, orient="records", lines=True, index=False)
df_test.to_json(TEST_PATH, orient="records", lines=True, index=False)

create_repo(
    ORGANIZATION+REPO_NAME, 
    repo_type="dataset"
)

upload_file(
    path_or_fileobj=TRAIN_PATH, 
    path_in_repo=TRAIN_PATH, 
    repo_id=ORGANIZATION + REPO_NAME, 
    repo_type="dataset"
)
os.system(f"rm {TRAIN_PATH}")

upload_file(
    path_or_fileobj=TEST_PATH, 
    path_in_repo=TEST_PATH, 
    repo_id=ORGANIZATION + REPO_NAME, 
    repo_type="dataset"
)
os.system(f"rm {TEST_PATH}")