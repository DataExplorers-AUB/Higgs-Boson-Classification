import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

frame_names = ["Higgs boson","lepton pT", "lepton eta", "lepton phi", "missing energy magnitude", "missing energy phi", "jet 1 pt",
               "jet 1 eta", "jet 1 phi", "jet 1 b-tag", "jet 2 pt", "jet 2 eta", "jet 2 phi", "jet 2 b-tag", "jet 3 pt",
               "jet 3 eta", "jet 3 phi", "jet 3 b-tag", "jet 4 pt", "jet 4 eta", "jet 4 phi", "jet 4 b-tag", "m jj",
               "m jjj", "m lv", "m jlv", "m bb", "m wbb", "m wwbb"]
data = pd.read_csv("HIGGS_train.csv", names=frame_names)

pd.set_option('display.max_columns', None)

data["Higgs boson"] = data["Higgs boson"].astype('category').cat.codes
print(data.head().to_string(index=False, justify='center'))
data.describe()

for feature in frame_names[1:]:
  sns.histplot(data=data, x=feature, hue=frame_names[0], element='bars')
  plt.title(feature)
  plt.show()

