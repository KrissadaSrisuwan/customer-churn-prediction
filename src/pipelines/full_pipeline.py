from src.data.load_data import load_config, load_data, save_data
from src.data.preprocess import preprocess

config = load_config("configs/config.yaml")

raw_df = load_data(config["raw_data_path"])

clean_df = preprocess(raw_df)

save_data(clean_df, config["clean_data_path"])