import socket
import threading

from get_ip_address import get_local_ip

def handle_client(conn, addr):
    try:
        counter = 0
        print(f"クライアント {addr} が接続しました")
        while True:
            data = conn.recv(1024)
            if not data:
                continue
            print(f"受信したデータ(count-{counter}): {data.decode()}")
            counter += 1
    except Exception as e:
        print(f"クライアント {addr} の処理中にエラーが発生しました: {e}")
    finally:
        conn.close()
        print(f"クライアント {addr} との接続を閉じました")

def start_server():
    host = get_local_ip()
    if not host:
        print("有効なIPアドレスを取得できませんでした。ネットワーク接続を確認してください。")
        return
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            s.listen()
            print(f"サーバーが {host}:{port} で起動しました")
            
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
        except Exception as e:
            print(f"サーバーの起動中にエラーが発生しました: {e}")

def start_client():
    host = input("サーバーのIPアドレスを入力してください: ")
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"サーバー {host}:{port} に接続しました")
            
            while True:
                message = input("サーバーに送信するメッセージを入力してください（終了するには 'quit' と入力）: ")
                if message.lower() == 'quit':
                    break
                s.sendall(message.encode())
                data = s.recv(1024)
                print(f"サーバーからの応答: {data.decode()}")
        except ConnectionRefusedError:
            print("サーバーに接続できませんでした。サーバーが起動しているか確認してください。")
        except Exception as e:
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        start_server()
    elif len(sys.argv) > 1 and sys.argv[1] == "client":
        start_client()