import pandas as pd
from utils import FEATURES

pd.set_option("display.max_columns", None)

def read_data(file_path):
    data = pd.read_csv(file_path, names=FEATURES.array, low_memory=False)
    data["Higgs boson"] = data["Higgs boson"].astype("category").cat.codes
    
    # Handle invalid data types
    data = convert_invalid_types(data)

    # Drop rows with missing values
    data.dropna(inplace=True)

    return data

def convert_invalid_types(data):
    object_cols = data.select_dtypes(include=["object"])
    mixed_type_cols = object_cols.columns[object_cols.apply(pd.Series.nunique) > 1]
    for col in mixed_type_cols:
        data[col] = pd.to_numeric(data[col].str.replace('"',''), errors="coerce")
    return data
