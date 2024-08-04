import os
from dotenv import load_dotenv
load_dotenv()

import network
import socket
from time import sleep

# Wi-Fi設定
SSID = os.environ["WIFI-SSID"]
PASSWORD = os.environ["WIFI-PASSWORD"]

# ネットワーク設定
LISTEN_IP = "192.168.1.50"  # 全てのインターフェースでリッスン
LISTEN_PORT = 8620
SEND_IP = "192.168.1.44"  # 端末3（PC）のIP
SEND_PORT = 65432

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        print("Wi-Fi接続を待っています...")
        sleep(1)

    print("Wi-Fi接続成功:")
    print(wlan.ifconfig())

def main():
    connect_wifi()
    listen_socket = socket.socket()
    listen_socket.bind((LISTEN_IP, LISTEN_PORT))
    listen_socket.listen(1)
    print(f"ポート{LISTEN_PORT}でリッスン中...")

    # send_socket = socket.socket()

    while True:
        conn, addr = listen_socket.accept()
        print(f"接続元: {addr}")

        try:
            # send_socket.connect((SEND_IP, SEND_PORT))

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"受信データ: {data.decode()}")
                # send_socket.send(data)
                # print("データ転送完了")

        except OSError as e:
            print(f"エラー発生: {e}")

        finally:
            conn.close()
            # send_socket.close()
            # send_socket = socket.socket()

if __name__ == "__main__":
    main()