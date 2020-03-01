from pathlib import Path
import pandas as pd

PROJECT_DIR = str(Path(__file__).resolve().parents[2])

file_path = str(PROJECT_DIR) + "/data/raw/" + "turnstile_200104.txt"
assert file_path == "/Users/erik/metis/projects/1/mtacular/data/raw/turnstile_200104.txt"

df = pd.read_csv(file_path)

