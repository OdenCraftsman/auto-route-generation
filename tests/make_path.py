import matplotlib.pyplot as plt
import time

def create_square_perimeter(size):
    """領域の外周を作成する関数"""
    perimeter = set()
    for x in range(size):
        perimeter.add((x, 0))
        perimeter.add((x, size-1))
    for y in range(1, size-1):
        perimeter.add((0, y))
        perimeter.add((size-1, y))
    return perimeter

def generate_interior_points(size):
    """内部のドットを出力する関数"""
    return {(x, y) for x in range(1, size-1) for y in range(1, size-1)}

def get_start_point(points):
    """左下を出力する関数"""
    return min(points, key=lambda p: (p[0], p[1]))

def get_next_point(current_point, size, visited):
    """今の座標から次の座標を出力する関数"""
    x, y = current_point
    candidates = []
    if x % 2 == 0:  # 偶数列
        if y < size - 1 and (x, y+1) not in visited:
            candidates.append((x, y+1))  # 上に移動
        elif x < size - 1:
            candidates.append((x+1, y))  # 右に移動
    else:  # 奇数列
        if y > 0 and (x, y-1) not in visited:
            candidates.append((x, y-1))  # 下に移動
        elif x < size - 1:
            candidates.append((x+1, y))  # 右に移動

    return candidates[0] if candidates else None

def plot_square_with_path(size, perimeter, interior_points):
    """pltで描画する関数"""
    plt.ion()  # インタラクティブモードをオンにする
    fig, ax = plt.subplots(figsize=(5, 5))

    # 外周を描画
    perimeter_x, perimeter_y = zip(*perimeter)
    ax.plot(perimeter_x, perimeter_y, 'b.', alpha=0.5, label='Perimeter')
    
    # 内部の点を描画
    interior_x, interior_y = zip(*interior_points)
    ax.scatter(interior_x, interior_y, color='red', s=20, alpha=0.5, label='Interior Points')
    # 経路を描画するための空のラインを作成
    path_line, = ax.plot([], [], 'g-', alpha=0.7, label='Path')
    # 現在の点を表す散布図を作成
    current_point_scatter = ax.scatter([], [], color='green', s=100, label='Current Point')

    ax.set_title(f"Path in {size}x{size} Square")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend()

    plt.tight_layout()
    return fig, ax, path_line, current_point_scatter

# メインのループ
if __name__ == "__main__":
    square_size = 10

    perimeter = create_square_perimeter(square_size)
    interior_points = generate_interior_points(square_size)
    all_points = perimeter.union(interior_points)
    start_point = get_start_point(all_points)

    fig, ax, path_line, current_point_scatter = plot_square_with_path(square_size, perimeter, interior_points)

    path = [start_point]
    current_point = start_point
    visited = set([start_point])

    while len(visited) < len(all_points):
        print(f"Current point: {current_point}")

        # 経路を更新
        path_x, path_y = zip(*path)
        path_line.set_data(path_x, path_y)
        # 現在の点を更新
        current_point_scatter.set_offsets([current_point])
        # 描画を更新
        fig.canvas.draw()
        fig.canvas.flush_events()
        # 0.2秒待機
        time.sleep(0.2)

        # 次の点を取得
        next_point = get_next_point(current_point, square_size, visited)

        path.append(next_point)
        visited.add(next_point)
        current_point = next_point

    plt.ioff()  # インタラクティブモードをオフにする
    plt.show()

print("Program ended.")