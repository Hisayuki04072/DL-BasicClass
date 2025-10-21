from utils.function import add

def count_word(s, w):
    """
        文字列内の文字数を数える関数
    """
    
    assert isinstance(s, str) # 第一引数の型をチェック
    assert isinstance(w, str) and len(w) == 1 # 第二引数の型と文字列の長さをチェック
    ret = 0
    for i in range(len(s)):
        if s[i] == w:
            ret = add(ret, 1) # 一致したとき加算
    return ret