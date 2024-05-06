import numpy as np

# 定义点的坐标
points = np.array([[1.90, 0.97],
                    [1.76, 0.84],
                    [2.32, 1.63],
                    [2.31, 2.09],
                    [1.14, 2.11],
                    [5.02, 3.02],
                    [5.74, 3.84],
                    [2.25, 3.47],
                    [4.71, 3.60],
                    [3.17, 4.96]])

# 初始化簇中心
center1 = np.array([1.90, 0.97])
center2 = np.array([1.76, 0.84])

# 计算距离
def distance(point, center):
    return np.sqrt(np.sum((point - center) ** 2))

# 分配点到簇
def assign_points(points, center1, center2):
    cluster1 = []
    cluster2 = []
    for point in points:
        dist1 = distance(point, center1)
        dist2 = distance(point, center2)
        if dist1 < dist2:
            cluster1.append(point)
        else:
            cluster2.append(point)
    return np.array(cluster1), np.array(cluster2)

# 更新簇中心
def update_centers(cluster1, cluster2):
    center1 = np.mean(cluster1, axis=0)
    center2 = np.mean(cluster2, axis=0)
    return center1, center2

# 迭代聚类过程
while True:
    cluster1, cluster2 = assign_points(points, center1, center2)
    new_center1, new_center2 = update_centers(cluster1, cluster2)
    if np.allclose(new_center1, center1) and np.allclose(new_center2, center2):
        break
    center1, center2 = new_center1, new_center2

# 打印结果
print("Final cluster 1 center:", center1)
print("Final cluster 2 center:", center2)
print("Cluster 1 points:", cluster1)
print("Cluster 2 points:", cluster2)
