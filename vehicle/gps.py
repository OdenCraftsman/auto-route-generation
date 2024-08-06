import re
from micropyGPS import MicropyGPS

class GPS:
    """
    NMEAセンテンスをパースし、gpsデータを作成するためのクラス
    sentence => NMEAセンテンス
    """
    def __init__(self, ):
        self.gga_gps = MicropyGPS(location_formatting="dd")
        self.rmc_gps = MicropyGPS(location_formatting="dd")

    #################### ▼property▼ ####################
    @property
    def location(self):
        latitude = f"{self.gga_gps.latitude[0]}{self.gga_gps.latitude[1]}"
        longitude = f"{self.gga_gps.longitude[0]}{self.gga_gps.longitude[1]}"
        return (latitude, longitude)
    #################### ▲property▲ ####################

    #################### ▼function▼ ####################
    def update_sentence(self, sentences):
        sentence_list = self.split_sentences(sentences)
        for sentence in sentence_list:
            sentenceID = self.get_sentenceID(sentence)
            if sentenceID == 'GGA':
                for char in sentence:
                    self.gga_gps.update(char)
            elif sentenceID == 'RMC':
                for char in sentence:
                    self.rmc_gps.update(char)
    def split_sentences(self, sentences):
        """
        複数のNMEAセンテンスを含む文字列を個別のセンテンスに分割する関数

        :param nmea_string: 複数のNMEAセンテンスを含む文字列
        :return: 個別のNMEAセンテンスのリスト
        """
        # 正規表現を使用してセンテンスを分割
        # $で始まり、改行文字（\r\n または \n）で終わるパターンを検索
        pattern = r'\$.*?(?:\r\n|\n)'
        sentences = re.findall(pattern, sentences, re.DOTALL)
        # 空白文字を取り除き、各センテンスの末尾の改行文字を削除
        sentences = [sentence.strip() for sentence in sentences]
        return sentences
    def get_sentenceID(self, sentence):
        """
        NMEAセンテンスから3桁のセンテンスIDを抽出する関数

        :param sentence: NMEAセンテンス文字列
        :return: 3桁のセンテンスID または None（無効なセンテンスの場合）
        """
        # 正規表現パターン: $で始まり、2文字の任意の文字、その後に3文字の英数字が続くパターン
        pattern = r'^\$..([A-Z0-9]{3})'
        match = re.match(pattern, sentence)
        if match:
            return match.group(1)
        else:
            return None
    #################### ▲function▲ ####################

if __name__ == "__main__":
    sentences = """
    $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
    $GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
    """
    gps = GPS()
    gps.update_sentence(sentences)
    print(gps.location)