import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white", font_scale=0.5)


def show_distribution(data, features, hue, rows=4, cols=7, bins=50):
    fig, axes = plt.subplots(rows, cols)
    for i in range(len(features)):
        sns.histplot(
            data=data,
            x=features[i],
            hue=hue,
            bins=bins,
            ax=axes[i//cols][i % cols],
            element="step",
            stat="proportion"
        )

    fig.tight_layout(pad=0)
    fig.set_tight_layout(True)
    plt.show()

def show_heatmap(data):
    correlation = data.corr()
    sns.heatmap(correlation, annot=True)
    plt.show()


def show_jet_pairplot(data, hue, rows=100, start_col=6, end_col=22):
    sns.pairplot(data=data.iloc[:rows, [0] +
                 list(range(start_col, end_col+1))], hue=hue)
    plt.show()

def print_distribution(data):
    print(data.describe())
