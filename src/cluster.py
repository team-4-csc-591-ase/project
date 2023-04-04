import warnings

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.tree import DecisionTreeClassifier, plot_tree

warnings.filterwarnings("ignore")


def cluster(x_train, y_train, x_test, y_test):
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
        pipe = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="mean")),
                (
                    "kmeans",
                    KMeans(
                        n_clusters=k,
                        init="k-means++",
                        max_iter=300,
                        n_init=10,
                        random_state=0,
                    ),
                ),
            ]
        )

        # fit the pipeline to the data
        pipe.fit(x_train)
        wcss.append(pipe.named_steps["kmeans"].inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title("Elbow Method")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.show()


def kmeans_sway(X, k, r):
    """
    :param X: 2D array with n samples and n features
    :param k: number of clusters to be created
    :param r: between 0 and 1 representing the percentage of data to be used
    :return:
    """

    # Initialize KMeans
    kmeans = KMeans(n_clusters=k, random_state=r)

    # Fit the data to KMeans
    kmeans.fit(X)

    # Get the cluster assignments and centroids
    clusters = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Calculate the distances between each data point and its assigned centroid
    distances = np.zeros(X.shape[0])
    for i in range(X.shape[0]):
        distances[i] = np.linalg.norm(X[i] - centroids[clusters[i]])

    # Calculate the median distance for each cluster
    median_distances = np.zeros(k)
    for i in range(k):
        median_distances[i] = np.median(distances[clusters == i])

    # Calculate the sway for each data point
    sway = np.zeros(X.shape[0])
    for i in range(X.shape[0]):
        sway[i] = (distances[i] / median_distances[clusters[i]]) ** 2

    # Update the weights for each data point
    weights = np.ones(X.shape[0])
    for i in range(X.shape[0]):
        for j in range(i + 1, X.shape[0]):
            if clusters[i] != clusters[j]:
                d = np.linalg.norm(X[i] - X[j])
                if (
                    d < median_distances[clusters[i]]
                    and d < median_distances[clusters[j]]
                ):
                    w = (1 - (d / (2 * median_distances[clusters[i]]))) ** 2
                    weights[i] += w
                    weights[j] += w

    # Fit the weighted data to KMeans
    kmeans.fit(X, sample_weight=weights)

    # Get the cluster assignments
    clusters = kmeans.labels_

    return clusters


# model = cluster(*split_x_y(read_csv()))

# print("Cluster centers:\n", model.cluster_centers_)
# print("Inertia:\n", model.inertia_)
# print("Iterations:\n", model.n_iter_)
# print("Labels:\n", model.labels_[:5])


def decision_tree(x_train, y_train, x_test, y_test):

    # discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    # y_train = discretizer.fit_transform(y_train.reshape(-1, 1)).ravel()

    # Create a KBinsDiscretizer object with 3 bins
    discretizer = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")

    # Fit and transform the data using the discretizer
    discretized_data = discretizer.fit_transform(y_train.values).reshape(-1)

    y_train = discretized_data.reshape(-1)
    clf = DecisionTreeClassifier()

    # print(type(y_train))

    # Train the classifier on the training data

    clf.fit(x_train, y_train)

    # Predict the classes of the testing data
    y_pred = clf.predict(x_test)

    # Calculate the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    # Visualize the decision tree
    plot_tree(clf)


def random_forest(x_train, y_train, x_test, y_test):

    discretizer = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
    # y = discretizer.fit_transform(y.values.reshape(-1, 1)).reshape(-1)
    # x_train, x_test, y_train, y_test = train_test_split(
    #     x, y, test_size=0.33, random_state=42
    # )
    # Create a random forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the classifier on the training data
    clf.fit(x_train, y_train)

    # Predict the classes of the testing data
    y_pred = clf.predict(x_test)

    # Calculate the accuracy of the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
