import matplotlib.pyplot as plt
import math

def generate_circular_perimeter(num_points, radius=1):
    coordinates = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        coordinates.append((x, y))
    return coordinates

def generate_square_perimeter(size):
    coordinates = []
    # 上辺
    for x in range(size):
        coordinates.append((x, 0))
    # 右辺
    for y in range(1, size):
        coordinates.append((size-1, y))
    # 下辺
    for x in range(size-2, -1, -1):
        coordinates.append((x, size-1))
    # 左辺
    for y in range(size-2, 0, -1):
        coordinates.append((0, y))
    return coordinates

def find_leftmost_bottom_point(coordinates):
    return min(coordinates, key=lambda coord: (coord[0], coord[1]))

def plot_perimeter_with_highlight(perimeter, highlight_point):
    """
    外周の配列と強調表示したい座標を受け取り、matplotlib（plt）に描画する関数

    :param perimeter: 外周の座標のリスト [(x1, y1), (x2, y2), ...]
    :param highlight_point: 強調表示したい座標 (x, y)
    """
    # 座標をx座標とy座標に分離
    x_coords, y_coords = zip(*perimeter)

    # プロットの作成
    plt.figure(figsize=(10, 10))
    
    # 外周を描画
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-', alpha=0.5)
    plt.scatter(x_coords, y_coords, color='red', s=10, alpha=0.5)

    # 強調したい点を描画
    plt.scatter(*highlight_point, color='green', s=200, zorder=5, edgecolor='black', linewidth=2)
    
    # 強調点にラベルを付ける
    plt.annotate(f'Highlighted: ({highlight_point[0]:.2f}, {highlight_point[1]:.2f})', 
                 xy=highlight_point, xytext=(10, 10), 
                 textcoords='offset points', ha='left', va='bottom',
                 bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    # グラフの設定
    plt.title("Perimeter with Highlighted Point", fontsize=14)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.grid(True, alpha=0.3)
    plt.axis('equal')

    # プロットの表示
    plt.show()

# 50x50のスクエアの外周座標を生成
perimeter = generate_circular_perimeter(50)

# 最も左にある座標を見つける
leftmost_point = find_leftmost_bottom_point(perimeter)

print(f"最も左にある座標: {leftmost_point}")

# 座標をx座標とy座標に分離
x_coords, y_coords = zip(*perimeter)

# プロットの作成
plt.figure(figsize=(5, 5))
plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-', alpha=0.5)  # 青い実線でプロット（透明度を下げる）
plt.scatter(x_coords, y_coords, color='red', s=10, alpha=0.5)  # 赤い点で各座標を表示（透明度を下げる）

# 最も左にある点を強調表示
plt.scatter(*leftmost_point, color='green', s=200, zorder=5, edgecolor='black', linewidth=2)  # 緑の大きな点で表示、黒い縁取り付き

# グラフの設定
plt.title("Circular Perimeter with 196 Points - Leftmost Point Highlighted", fontsize=14)
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.grid(True, alpha=0.3)  # グリッドの透明度を下げる
plt.axis('equal')  # x軸とy軸のスケールを同じに

# プロットの表示
plt.show()