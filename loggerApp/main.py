import socket

# ネットワーク設定
LISTEN_IP = "192.168.1.44"  # 全てのインターフェースでリッスン
LISTEN_PORT = 65432

def main():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind((LISTEN_IP, LISTEN_PORT))
    listen_socket.listen(1)
    print(f"ポート{LISTEN_PORT}でリッスン中...")

    while True:
        conn, addr = listen_socket.accept()
        print(f"接続元: {addr}")

        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"受信データ: {data.decode()}")

        except Exception as e:
            print(f"エラー発生: {e}")

        finally:
            conn.close()

if __name__ == "__main__":
    main()