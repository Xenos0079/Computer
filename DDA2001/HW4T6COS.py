def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def assign_clusters(points):
    global centroid1 , centroid2
    for point in points:
        if euclidean_distance(point, centroid1) <= euclidean_distance(point, centroid2):
            point[2] = 1
        else:
            point[2] = 2

def separate_clusters(points):
    global centroid1 , centroid2
    cluster1 = []
    cluster2 = []
    for point in points:
        if point[2] == 1:
            cluster1.append(point)
        else:
            cluster2.append(point)
    return cluster1, cluster2

def calculate_new_centroids(cluster1, cluster2):
    global centroid1 , centroid2
    centroid1 = [0, 0]  # 初始化新的中心点
    centroid2 = [0, 0]  # 初始化新的中心点
    for point in cluster1:
        centroid1[0] += point[0]
        centroid1[1] += point[1]
    for point in cluster2:
        centroid2[0] += point[0]
        centroid2[1] += point[1]
    if len(cluster1) != 0:
        centroid1[0] /= len(cluster1)
        centroid1[1] /= len(cluster1)
    if len(cluster2) != 0:
        centroid2[0] /= len(cluster2)
        centroid2[1] /= len(cluster2)
    return centroid1, centroid2

def k_means(points):
    global centroid1 , centroid2
    assign_clusters(points)
    for _ in range(10):
        cluster1, cluster2 = separate_clusters(points)
        centroid1, centroid2 = calculate_new_centroids(cluster1, cluster2)
        assign_clusters(points)
        print('Centroid 1:', centroid1)
        print('Centroid 2:', centroid2)

x1 = [1.90 , 0.97 , 0]
x2 = [1.76 , 0.84 , 0]
x3 = [2.32 , 1.63 , 0]
x4 = [2.31 , 2.09 , 0]
x5 = [1.14 , 2.11 , 0]
x6 = [5.02 , 3.02 , 0]
x7 = [5.74 , 3.84 , 0]
x8 = [2.25 , 3.47 , 0]
x9 = [4.71 , 3.60 , 0]
x0 = [3.17 , 4.96 , 0]

points = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x0]

centroid1 = x1
centroid2 = x0

k_means(points)


