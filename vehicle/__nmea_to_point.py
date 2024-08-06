from micropyGPS import MicropyGPS

def nmea_to_point(sentence):
    gps = MicropyGPS()

    for char in sentence:
        gps.update(char)

    if gps.latitude[0] and gps.longitude[0]:
        lat = gps.latitude[0] + gps.latitude[1] / 60
        lon = gps.longitude[0] + gps.longitude[1] / 60
    return (lat, lon)

if __name__ == "__main__":
    nmea_sentences = [
        "$GNGGA,092201.23,3720.5406801,N,13853.3035139,E,2,07,5.24,262.957,M,37.484,M,1.2,1115*6E",
        "$GNGGA,092201.34,3720.5406705,N,13853.3034720,E,2,07,5.24,262.991,M,37.484,M,1.3,1115*67"
    ]

    for sentence in nmea_sentences:
        point = nmea_to_point(sentence)
        print(point)