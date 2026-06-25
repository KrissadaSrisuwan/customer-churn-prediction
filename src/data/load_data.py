import yaml
import pandas as pd


def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_data(path):
    print("Data loaded successfully!")
    return pd.read_csv(path)

def save_data(df, path):
    df.to_csv(path, index=False)
    print(f"Data saved to: {path}")


if __name__ == "__main__":
    config = load_config("configs/config.yaml")
    df = load_data(config["raw_data_path"])