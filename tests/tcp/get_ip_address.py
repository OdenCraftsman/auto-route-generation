import netifaces

def get_local_ip():
    try:
        # Wi-FiインターフェースのIPアドレスを取得
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            if interface.startswith('en'):  # MacBookのWi-Fiインターフェースは通常'en0'や'en1'
                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses:
                    return addresses[netifaces.AF_INET][0]['addr']
    except Exception as e:
        print(f"IPアドレスの取得に失敗しました: {e}")
    return None


if __name__ == "__main__":
    ip = get_local_ip()
    if ip:
        print(f"IPアドレス: {ip}")