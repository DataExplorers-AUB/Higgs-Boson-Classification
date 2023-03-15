import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

frame_names = ["Higgs boson","lepton pT", "lepton eta", "lepton phi", "missing energy magnitude", "missing energy phi", "jet 1 pt",
               "jet 1 eta", "jet 1 phi", "jet 1 b-tag", "jet 2 pt", "jet 2 eta", "jet 2 phi", "jet 2 b-tag", "jet 3 pt",
               "jet 3 eta", "jet 3 phi", "jet 3 b-tag", "jet 4 pt", "jet 4 eta", "jet 4 phi", "jet 4 b-tag", "m jj",
               "m jjj", "m lv", "m jlv", "m bb", "m wbb", "m wwbb"]
data = pd.read_csv("HIGGS_train.csv", names=frame_names, low_memory=False)

pd.set_option("display.max_columns", None)

data["Higgs boson"] = data["Higgs boson"].astype("category").cat.codes

# convert mixed values to numeric values or Nan if n/a
object_cols = data.select_dtypes(include=["object"])
mixed_type_cols = object_cols.columns[object_cols.apply(pd.Series.nunique) > 1]

for col in mixed_type_cols:
    data[col] = pd.to_numeric(data[col].str.replace('"',''), errors="coerce")

# drop null values
data = data.dropna()

print(data.shape)
data.describe()

for feature in frame_names[1:]:
    sns.histplot(data=data, x=feature, hue=frame_names[0], element="bars")
    plt.title(feature)
    plt.show()