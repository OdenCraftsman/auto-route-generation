import matplotlib.pyplot as plt
import time
import math

def create_perimeter():
    coordinates = []
    # ========== circle ==========
    # radius = 50
    # num_points = 100
    # for i in range(num_points):
    #     angle = 2 * math.pi * i / num_points
    #     x = radius * math.cos(angle)
    #     y = radius * math.sin(angle)
    #     coordinates.append((int(x), int(y)))

    # ========== square ==========
    size = 100
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


def get_next_coordinate(current_coord, required_coords, visited_coords):
    """
    蛇行パターンで次の座標を決定する関数

    :param required_coords: 通らなければいけない座標のセット
    :param current_coord: 現在の座標 (x, y)
    :param visited_coords: これまでに通った座標のリスト
    :return: 次に通る座標 (x, y)、または全ての必要な座標を訪れた場合はNone
    """
    if not required_coords - set(visited_coords):
        return None  # 全ての必要な座標を訪れた場合

    x, y = current_coord
    directions = [(0, 1), (0, -1), (1, 0)]  # 上、下、右の順番で移動を試みる

    # 現在の列が偶数か奇数かで上下の優先順位を変える
    if x % 2 == 0:
        directions = [(0, 1), (0, -1), (1, 0)]  # 偶数列：上、下、右
    else:
        directions = [(0, -1), (0, 1), (1, 0)]  # 奇数列：下、上、右

    for dx, dy in directions:
        new_coord = (x + dx, y + dy)
        if new_coord in required_coords and new_coord not in visited_coords:
            return new_coord

    # 必要な座標がない場合、単純に次の座標に移動
    for dx, dy in directions:
        new_coord = (x + dx, y + dy)
        if new_coord in required_coords:
            return new_coord

    # どの方向にも進めない場合（通常ここには到達しないはず）
    return None

def get_perimeter_size(perimeter):
    """
    座標の集合から領域の横の長さと縦の長さを計算する関数

    :param coordinates: (x, y) 形式の座標のセット
    :return: (横の長さ, 縦の長さ) のタプル
    """
    if not perimeter:
        return (0, 0)  # 空の集合の場合

    # x座標とy座標を分離
    x_coords, y_coords = zip(*perimeter)

    # x座標の最小値と最大値を見つける
    min_x, max_x = min(x_coords), max(x_coords)

    # y座標の最小値と最大値を見つける
    min_y, max_y = min(y_coords), max(y_coords)

    # 長さを計算（最大値 - 最小値 + 1 で点の数を数える）
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    return (width, height)

def make_graph(perimeter, interior_points):
    """pltで描画する関数"""
    plt.ion()  # インタラクティブモードをオンにする
    fig, ax = plt.subplots(figsize=(5, 5))

    # 外周を描画
    perimeter_x, perimeter_y = zip(*perimeter)
    ax.plot(perimeter_x, perimeter_y, 'b.', alpha=0.5, label='Perimeter')

    # 内部の点を描画
    interior_x, interior_y = zip(*interior_points)
    ax.scatter(interior_x, interior_y, color='red', s=20, alpha=0.5, label='Interior Points')

    ax.set_title(f"Path in Square")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    plt.tight_layout()
    return fig, ax

# メインのループ
if __name__ == "__main__":
    perimeter = create_perimeter()
    perimeter_size = [100, 100]
    print(f"Perimeter: {perimeter}")
    print(f"Perimeter size: {perimeter_size}")

    interior_points = find_interior_points(perimeter)
    all_points = set(perimeter).union(interior_points)
    print("All points: ", all_points)
    start_point = find_leftmost_bottom_point(perimeter)

    fig, ax = make_graph(perimeter, interior_points)

    path = [start_point]
    current_point = start_point
    visited = set([start_point])

    while len(visited) < len(all_points):
        print(f"Current point: {current_point}")

        # 現在の点を更新
        ax.scatter(*current_point, color='green', zorder=5, label='Current Point')
        # 描画を更新
        fig.canvas.draw()
        fig.canvas.flush_events()
        # 0.2秒待機
        time.sleep(0.001)

        # 次の点を取得
        next_point = get_next_coordinate(current_point, all_points, visited)

        path.append(next_point)
        visited.add(next_point)
        current_point = next_point

    plt.ioff()  # インタラクティブモードをオフにする
    plt.show()

print("Program ended.")