import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
import math
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt


from src.pre_process import (
    CATEGORICAL_COLUMNS,
    DROP_COLUMNS,
    pre_process,
    standardscaler,
)

DATA_DIR = "../etc/data/"


def get_all_files():
    files_dict = {}
    for file_name in os.listdir(DATA_DIR):
        files_dict[file_name] = f"{DATA_DIR}{file_name}"
    return files_dict


def read_csv():
    data_files = get_all_files()
    _data_dict = {}
    for file_name, file_path in data_files.items():
        data = pd.read_csv(file_path, skipinitialspace=True)
        data.replace("?", np.nan, inplace=True)
        categorical_columns = CATEGORICAL_COLUMNS.get(file_name, None)
        columns_to_drop = DROP_COLUMNS.get(file_name, None)

        try:
            data, updated_cols = pre_process(
                data=data,
                categorical_columns=categorical_columns,
                columns_to_drop=columns_to_drop,
            )
            data = standardscaler(
                data=data, columns=categorical_columns, updated_cols=updated_cols
            )
            _data_dict[file_name] = data
        except Exception as e:
            print()
            print(f"Error processing {file_name}: {e}")
    return _data_dict


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
    # _model = KMeans()
    # _model.fit(x_train, y_train)
    # # print the centroids of the clusters
    # # print(_model.cluster_centers_)
    #
    # # predict the cluster labels for the data points
    # print(_model.labels_)

    # pipe = Pipeline([('imputer', SimpleImputer(strategy='mean')),
    #                  ('kmeans', KMeans(n_clusters=5))])

    # fit the pipeline to the data
    # pipe.fit(x_train)

    # predict the cluster labels for the data points
    # print(pipe.named_steps['kmeans'].cluster_centers_)
    # print(pipe.named_steps['kmeans'].labels_)

    wcss = []
    for k in range(1, 11):
        pipe = Pipeline([('imputer', SimpleImputer(strategy='mean')),
                         ('kmeans', KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0))])

        # fit the pipeline to the data
        pipe.fit(x_train)
        wcss.append(pipe.named_steps['kmeans'].inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()



# model = cluster(*split_x_y(read_csv()))

# print("Cluster centers:\n", model.cluster_centers_)
# print("Inertia:\n", model.inertia_)
# print("Iterations:\n", model.n_iter_)
# print("Labels:\n", model.labels_[:5])

data_dict = read_csv()
for i in data_dict:
    print(f"File Name: {i}")
    x, y = split_x_y(data_dict[i])
    print("Printing X:")
    # print(x.head())
    print("Printing Y:")
    # print(y.head())

    # df = pd.read_csv(DATA_DIR+i)
    #
    # print(df.isnull().sum())

    cluster(x,y)
