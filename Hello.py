import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 定义正方体的8个顶点
vertices = np.array([
    [0, 0, 0],  # 顶点0
    [1, 0, 0],  # 顶点1
    [1, 1, 0],  # 顶点2
    [0, 1, 0],  # 顶点3
    [0, 0, 1],  # 顶点4
    [1, 0, 1],  # 顶点5
    [1, 1, 1],  # 顶点6
    [0, 1, 1]   # 顶点7
])

# 定义正方体的12条边（由顶点索引表示）
edges = [
    [vertices[0], vertices[1], vertices[2], vertices[3], vertices[0]],  # 底面
    [vertices[4], vertices[5], vertices[6], vertices[7], vertices[4]],  # 顶面
    [vertices[0], vertices[4]],  # 侧面边
    [vertices[1], vertices[5]],  # 侧面边
    [vertices[2], vertices[6]],  # 侧面边
    [vertices[3], vertices[7]]   # 侧面边
]

# 创建3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制正方体的边
for edge in edges:
    ax.plot3D(*zip(*edge), color="blue")

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置图形显示范围
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# 显示图形
plt.show()


