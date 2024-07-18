import matplotlib.pyplot as plt

def generate_square_perimeter(size):
    return ([(x, 0) for x in range(size)] + 
            [(size-1, y) for y in range(1, size)] + 
            [(x, size-1) for x in range(size-2, -1, -1)] + 
            [(0, y) for y in range(size-2, 0, -1)])

def find_interior_points(perimeter):
    min_x = min(x for x, y in perimeter)
    max_x = max(x for x, y in perimeter)
    min_y = min(y for x, y in perimeter)
    max_y = max(y for x, y in perimeter)
    
    return [(x, y) for x in range(min_x + 1, max_x) for y in range(min_y + 1, max_y)]

def generate_snake_pattern_path(size):
    path = []
    for x in range(size):
        if x % 2 == 0:  # 偶数列は下から上へ
            for y in range(size):
                path.append((x, y))
        else:  # 奇数列は上から下へ
            for y in range(size - 1, -1, -1):
                path.append((x, y))
    return path

def plot_square_with_snake_path_realtime(size, path, delay=0.1):
    perimeter = generate_square_perimeter(size)
    interior_points = find_interior_points(perimeter)
    all_points = set(perimeter + interior_points)

    plt.ion()  # インタラクティブモードをオンにする
    fig, ax = plt.subplots(figsize=(5, 5))

    # 外周を描画
    x_coords, y_coords = zip(*perimeter)
    ax.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-', alpha=0.5, label='Perimeter')

    # 全ての点を描画
    all_x_coords, all_y_coords = zip(*all_points)
    ax.scatter(all_x_coords, all_y_coords, color='red', s=20, alpha=0.5, label='All Points')

    # 現在位置を表す点と経路を表す線を初期化
    current_point, = ax.plot([], [], 'go', markersize=10, label='Current Position')
    path_line, = ax.plot([], [], 'g-', alpha=0.5)

    ax.set_title(f"Snake Pattern Path Through {size}x{size} Square")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    plt.draw()
    plt.pause(0.1)

    path_x = []
    path_y = []

    for x, y in path:
        path_x.append(x)
        path_y.append(y)

        current_point.set_data([x], [y])
        path_line.set_data(path_x, path_y)

        plt.draw()
        plt.pause(delay)

    plt.ioff()  # インタラクティブモードをオフにする
    plt.show()

# 使用例
if __name__ == "__main__":
    square_size = 10

    # 蛇行パターンの経路を生成
    snake_path = generate_snake_pattern_path(square_size)

    # リアルタイムでプロットを表示
    plot_square_with_snake_path_realtime(square_size, snake_path, delay=0.1)