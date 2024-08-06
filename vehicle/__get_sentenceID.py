import re

def get_sentenceID(sentence):
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

# 使用例
sentences = [
    "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47",
    "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A",
    "$GPGSA,A,3,04,05,,09,12,,,24,,,,,2.5,1.3,2.1*39",
    "INVALID SENTENCE",
]

for sentence in sentences:
    sentence_id = get_sentenceID(sentence)
    if sentence_id:
        print(f"センテンス '{sentence[:20]}...' のID: {sentence_id}")
    else:
        print(f"無効なセンテンス: {sentence[:20]}...")