import re

def split_nmea_sentences(nmea_string):
    """
    複数のNMEAセンテンスを含む文字列を個別のセンテンスに分割する関数

    :param nmea_string: 複数のNMEAセンテンスを含む文字列
    :return: 個別のNMEAセンテンスのリスト
    """
    # 正規表現を使用してセンテンスを分割
    # $で始まり、改行文字（\r\n または \n）で終わるパターンを検索
    pattern = r'\$.*?(?:\r\n|\n)'
    sentences = re.findall(pattern, nmea_string, re.DOTALL)
    # 空白文字を取り除き、各センテンスの末尾の改行文字を削除
    sentences = [sentence.strip() for sentence in sentences]
    return sentences

if __name__ == "__main__":
    nmea_data = """$GPGGA,115056.42,3720.5287631,N,13853.3167176,E,2,12,0.86,300.456,M,37.485,M,0.4,1115*70
$GPRMC,115056.53,A,3720.5287278,N,13853.3167620,E,0.159,137.67,060824,,,D,V*18
$GPGGA,115056.53,3720.5287278,N,13853.3167620,E,2,12,0.86,300.431,M,37.485,M,0.5,1115*7D
$GPRMC,115056.64,A,3720.5286797,N,13853.3167978,E,0.310,137.67,060824,,,D,V*14
$GPGGA,115056.64,3720.5286797,N,13853.3167978,E,2,12,0.86,300.430,M,37.485,M,0.6,1115*7C
$GPRMC,115056.75,A,3720.5286522,N,13853.3168205,E,0.144,137.67,060824,,,D,V*15
$GPGGA,115056.75,3720.5286522,N,13853.3168205,E,2,12,0.86,300.425,M,37.485,M,0.8,1115*74
$GPRMC,115056.87,A,3720.5286255,N,13853.3168502,E,0.102,137.67,060824,,,D,V*1D
$GPGGA,115056.87,3720.5286255,N,13853.3168502,E,2,12,0.86,300.376,M,37.485,M,0.9,1115*7E
$GPRMC,115056.98,A,3720.528596,
    """

    split_sentences = split_nmea_sentences(nmea_data)

    for i, sentence in enumerate(split_sentences, 1):
        print(f"Sentence {i}: {sentence}")