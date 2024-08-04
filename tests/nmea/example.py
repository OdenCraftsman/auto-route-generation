from micropyGPS import MicropyGPS

# GPSオブジェクトを初期化（パラメータ付き）
my_gps = MicropyGPS(location_formatting='dd', local_offset=9)

# 以下、前回のコード例と同様...

def parse_sentence(sentence):
    for char in sentence:
        my_gps.update(char)

nmea_sentence = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
parse_sentence(nmea_sentence)

print(f"Latitude: {my_gps.latitude_string()}")
print(f"Longitude: {my_gps.longitude_string()}")
print(f"Time Zone: UTC+{my_gps.local_offset}")

# その他の情報取得は前回と同様...