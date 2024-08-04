import network
import time

def connect_wifi(ssid, password, max_wait=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wi-Fi接続を待つ
    wait = 0
    while wait < max_wait:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        print('Waiting for connection...')
        time.sleep(1)
        wait += 1
    
    # 接続結果の確認
    if wlan.status() != 3:
        raise RuntimeError('Wi-Fi connection failed')
    else:
        print('Connected')
        status = wlan.ifconfig()
        print('IP = ' + status[0])
    
    return status[0]  # IPアドレスを返す

# 使用例
try:
    ip = connect_wifi('TP-Link_3DA0', '69714993')
    print(f'Device IP: {ip}')
except Exception as e:
    print(f'Failed to connect to Wi-Fi: {e}')
