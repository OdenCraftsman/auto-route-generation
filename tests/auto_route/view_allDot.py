import matplotlib.pyplot as plt
import math

def generate_circular_perimeter(num_points, radius=25):
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


def find_interior_points(perimeter):
    # 外周の境界を決定
    min_x = min(x for x, y in perimeter)
    max_x = max(x for x, y in perimeter)
    min_y = min(y for x, y in perimeter)
    max_y = max(y for x, y in perimeter)

    # 内部の点を格納するリスト
    interior_points = []

    # 各マスをチェック
    for x in range(math.floor(min_x), math.ceil(max_x) + 1):
        for y in range(math.floor(min_y), math.ceil(max_y) + 1):
            if is_point_inside(x, y, perimeter):
                interior_points.append((x, y))

    return interior_points

def is_point_inside(x, y, perimeter):
    n = len(perimeter)
    inside = False
    p1x, p1y = perimeter[0]
    for i in range(n + 1):
        p2x, p2y = perimeter[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def plot_perimeter_with_highlight(perimeter, highlight_point, interior_points=None):
    """
    外周の配列、強調表示したい座標、および内部の点（オプション）を受け取り、matplotlib（plt）に描画する関数

    :param perimeter: 外周の座標のリスト [(x1, y1), (x2, y2), ...]
    :param highlight_point: 強調表示したい座標 (x, y)
    :param interior_points: 内部の点のリスト [(x1, y1), (x2, y2), ...], デフォルトはNone
    """
    # 座標をx座標とy座標に分離
    x_coords, y_coords = zip(*perimeter)

    # プロットの作成
    plt.figure(figsize=(5, 5))
    
    # 内部の点を描画（もし提供されていれば）
    if interior_points and len(interior_points) > 0:
        int_x_coords, int_y_coords = zip(*interior_points)
        plt.scatter(int_x_coords, int_y_coords, color='lightblue', s=5, alpha=0.5, label='Interior Points')

    # 外周を描画
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-', alpha=0.5, label='Perimeter')
    plt.scatter(x_coords, y_coords, color='red', s=10, alpha=0.5)

    # 強調したい点を描画
    plt.scatter(*highlight_point, color='green', s=100, zorder=5, edgecolor='black', linewidth=2, label='Highlighted Point')

    # グラフの設定
    plt.title("Perimeter with Highlighted Point and Interior Points", fontsize=14)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()

    # プロットの表示
    plt.show()


if __name__ == '__main__':
    # 50x50のスクエアの外周座標を生成
    perimeter = generate_circular_perimeter(50)
    print(f"perimeter: {perimeter} ¥n")
    # 最も左にある座標を見つける
    highlight_point = find_leftmost_bottom_point(perimeter)
    print(f"highlight_point: {highlight_point} ¥n")
    # 格子状のドットを取得
    interior_points = find_interior_points(perimeter)
    print(f"interior_points: {interior_points} ¥n")

    plot_perimeter_with_highlight(perimeter, highlight_point, interior_points)