import pandas as pd
from data.read import read_data
from data import visualize
from utils import FEATURES

data = read_data("HIGGS_train.csv")

print(data.shape)

visualize.print_distribution(data)

visualize.show_distribution(data, FEATURES.array[1:], FEATURES.Higgs_boson)
visualize.show_distribution(data, FEATURES.array[6:22], FEATURES.Higgs_boson, 4, 4, 50)
visualize.show_heatmap(data)

visualize.show_jet_pairplot(data, hue=FEATURES.Higgs_boson)