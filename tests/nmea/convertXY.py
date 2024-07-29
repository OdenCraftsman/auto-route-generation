import math
from micropyGPS import MicropyGPS
import matplotlib.pyplot as plt

nmea_sentences = []
with open('sample_data.txt', 'r') as file:
    nmea_sentences = file.readlines()
    nmea_sentences = [sentence for sentence in nmea_sentences if sentence.startswith('$GPRMC')]
print(nmea_sentences)


def process_nmea_sentences(sentences):
    gps = MicropyGPS()
    points = []

    for sentence in sentences:
        for char in sentence:
            gps.update(char)
        
        if gps.latitude[0] and gps.longitude[0]:
            lat = gps.latitude[0] + gps.latitude[1] / 60
            lon = gps.longitude[0] + gps.longitude[1] / 60
            points.append((lat, lon))

    return points

def latlon_to_xy(points):
    if not points:
        return []

    # 中心点（平均）を計算
    avg_lat = sum(p[0] for p in points) / len(points)
    avg_lon = sum(p[1] for p in points) / len(points)

    # 地球の平均半径（メートル）
    R = 6371000

    # 中心点をラジアンに変換
    avg_lat_rad = math.radians(avg_lat)
    avg_lon_rad = math.radians(avg_lon)

    xy_points = []
    for lat, lon in points:
        lat_rad = math.radians(lat)
        lon_rad = math.radians(lon)
        
        delta_lat = lat_rad - avg_lat_rad
        delta_lon = lon_rad - avg_lon_rad
        
        x = R * delta_lon * math.cos(avg_lat_rad)
        y = R * delta_lat
        
        xy_points.append((x, y))

    return xy_points

latlon_points = process_nmea_sentences(nmea_sentences)
xy_points = latlon_to_xy(latlon_points)

# データの抽出
x_coords, y_coords = zip(*xy_points)

# プロットの作成
plt.figure(figsize=(10, 8))
plt.scatter(x_coords, y_coords, c='blue', s=50, alpha=0.7)

# グラフの設定
plt.xlabel('X coordinate (meters)')
plt.ylabel('Y coordinate (meters)')
plt.grid(True)
plt.axis('equal')  # X軸とY軸のスケールを同じにする

# 最大距離の計算と表示
max_distance = max(math.sqrt(x**2 + y**2) for x, y in xy_points)
plt.text(0.05, 0.95, f'Max distance from center: {max_distance:.2f} m', 
         transform=plt.gca().transAxes, verticalalignment='top', 
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

print("Projected points (x, y) in meters:")
for i, (x, y) in enumerate(xy_points, 1):
    print(f"Point {i}: ({x:.2f}, {y:.2f})")

print(f"\nMaximum distance from center: {max_distance:.2f} meters")