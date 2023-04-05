import warnings

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.impute import SimpleImputer
# from sklearn.metrics import accuracy_score
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import KBinsDiscretizer, LabelEncoder
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.metrics import mean_squared_error

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

# def recursive_kmeans_sway(data, k, r=10):
#     """
#     Recursive K-Means clustering using sway method
#
#     Parameters:
#     X (pd.DataFrame): input data
#     k (int): number of clusters
#     r (int): number of times to run the K-Means algorithm
#
#     Returns:
#     clusters (list): list of cluster labels for each data point in X
#     """
#
#     # Initialize list of cluster labels
#     clusters = [-1] * len(data)
#
#     # Base case: only one cluster
#     if k == 1:
#         clusters = [0] * len(data)
#
#     # Recursive case
#     else:
#         # Run K-Means algorithm r times
#         kmeans = KMeans(n_clusters=k).fit(data)
#         labels = kmeans.labels_
#         centers = kmeans.cluster_centers_
#
#         # Calculate distances to cluster centers for each data point
#         distances = np.zeros((len(data), k))
#         for i in range(len(data)):
#             for j in range(k):
#                 distances[i][j] = np.linalg.norm(data.iloc[i] - centers[j])
#
#         # Find minimum distance for each data point
#         min_distances = distances.min(axis=1)
#
#         # Calculate sway for each cluster
#         sway = np.zeros(k)
#         for j in range(k):
#             cluster_j = data[labels == j]
#             if len(cluster_j) > 0:
#                 sway[j] = np.sum((min_distances[labels == j] ** 2) / len(cluster_j))
#
#         # Find cluster with maximum sway
#         max_sway_cluster = np.argmax(sway)
#
#         # Split data into two clusters
#         cluster_1 = data[labels == max_sway_cluster]
#         cluster_2 = data[labels != max_sway_cluster]
#
#         # Recursively cluster each subset
#         if len(cluster_1) > 0:
#             clusters_1 = recursive_kmeans_sway(cluster_1, k // 2, r)
#             for i in range(len(clusters_1)):
#                 if clusters_1[i] == 0:
#                     print("i=", i)
#                     clusters[labels == max_sway_cluster][i] = max_sway_cluster
#         if len(cluster_2) > 0:
#             clusters_2 = recursive_kmeans_sway(cluster_2, k - k // 2, r)
#             for i in range(len(clusters_2)):
#                 if clusters_2[i] == 0:
#                     clusters[labels != max_sway_cluster][i] = k - max_sway_cluster - 1
#     print("clusters =", clusters)
#     return clusters


# def kmeans_sway(X, k, r):
#     """
#     :param X: 2D array with n samples and n features
#     :param k: number of clusters to be created
#     :param r: between 0 and 1 representing the percentage of data to be used
#     :return:
#     """
#
#     # Initialize KMeans
#     kmeans = KMeans(n_clusters=k, random_state=r)
#
#     # Fit the data to KMeans
#     kmeans.fit(X)
#
#     # Get the cluster assignments and centroids
#     clusters = kmeans.labels_
#     centroids = kmeans.cluster_centers_
#
#     # Calculate the distances between each data point and its assigned centroid
#     distances = np.zeros(X.shape[0])
#     for i in range(X.shape[0]):
#         distances[i] = np.linalg.norm(X[i] - centroids[clusters[i]])
#
#     # Calculate the median distance for each cluster
#     median_distances = np.zeros(k)
#     for i in range(k):
#         median_distances[i] = np.median(distances[clusters == i])
#
#     # Calculate the sway for each data point
#     sway = np.zeros(X.shape[0])
#     for i in range(X.shape[0]):
#         sway[i] = (distances[i] / median_distances[clusters[i]]) ** 2
#
#     # Update the weights for each data point
#     weights = np.ones(X.shape[0])
#     for i in range(X.shape[0]):
#         for j in range(i + 1, X.shape[0]):
#             if clusters[i] != clusters[j]:
#                 d = np.linalg.norm(X[i] - X[j])
#                 if (
#                     d < median_distances[clusters[i]]
#                     and d < median_distances[clusters[j]]
#                 ):
#                     w = (1 - (d / (2 * median_distances[clusters[i]]))) ** 2
#                     weights[i] += w
#                     weights[j] += w
#
#     # Fit the weighted data to KMeans
#     kmeans.fit(X, sample_weight=weights)
#
#     # Get the cluster assignments
#     clusters = kmeans.labels_
#
#     return clusters


# model = cluster(*split_x_y(read_csv()))

# print("Cluster centers:\n", model.cluster_centers_)
# print("Inertia:\n", model.inertia_)
# print("Iterations:\n", model.n_iter_)
# print("Labels:\n", model.labels_[:5])


# def decision_tree(x_train, y_train, x_test, y_test):
#
#     print("x_train shape", x_train.shape)
#     print("y_train shape", y_train.shape)
#     # print(x_train.head())
#
#     # discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
#     # y_train = discretizer.fit_transform(y_train.reshape(-1, 1)).ravel()
#
#     # Create a KBinsDiscretizer object with 3 bins
#     discretizer = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
#
#     # Fit and transform the data using the discretizer
#     # y_train = discretizer.fit_transform(y_train.values).reshape(-1)
#     # print("y_train shape", y_train.shape)
#     # print("shape disc_Data", discretized_data.shape)
#     # y_train = discretized_data.reshape(248,)
#
#     # y_train = y_train.reshape(248, )
#     y_train = y_train.values.ravel()
#     print(y_train.shape)
#
#     label_encoder = LabelEncoder()
#     y_train = label_encoder.fit_transform(y_train)
#
#     clf = DecisionTreeClassifier()
#     # Train the classifier on the training data
#
#     clf.fit(x_train, y_train[:62])
#
#     # Predict the classes of the testing data
#     y_pred = clf.predict(x_test)
#
#     # Calculate the accuracy of the classifier
#     mse = mean_squared_error(y_test, y_pred)
#     print("MSE:", mse)
#
#
#     # Visualize the decision tree
#     plot_tree(clf)
#
#
# def random_forest(x_train, y_train, x_test, y_test):
#
#     discretizer = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
#     # y = discretizer.fit_transform(y.values.reshape(-1, 1)).reshape(-1)
#     # x_train, x_test, y_train, y_test = train_test_split(
#     #     x, y, test_size=0.33, random_state=42
#     # )
#     # Create a random forest classifier
#     clf = RandomForestClassifier(n_estimators=100, random_state=42)
#
#     # Train the classifier on the training data
#     clf.fit(x_train, y_train)
#
#     # Predict the classes of the testing data
#     y_pred = clf.predict(x_test)
#
#     # Calculate the accuracy of the classifier
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f"Accuracy: {accuracy:.2f}")
