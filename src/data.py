import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split


def read_csv():
    data = pd.read_csv("../etc/data/auto93.csv")

    # Add pre processing steps
    data = data[data.HpX != "?"]
    return data


def split_x_y(data):
    x, y = [], []
    for column_name in data.columns:
        if not column_name[-1].isalpha():
            y.append(column_name)
        else:
            x.append(column_name)
    return data[x], data[y]


def cluster(x, y):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=42
    )
    _model = KMeans()
    _model.fit(x_train, y_train)
    return _model


model = cluster(*split_x_y(read_csv()))

print("Cluster centers:\n", model.cluster_centers_)
print("Inertia:\n", model.inertia_)
print("Iterations:\n", model.n_iter_)
print("Labels:\n", model.labels_[:5])
