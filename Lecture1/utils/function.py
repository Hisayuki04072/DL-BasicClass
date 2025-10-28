
def add(a,b):
    """
    足し算を行う関数
    """    
    ret = a + b
    return ret


if __name__ == "__main__":
    test = add(2,3) == 5 # 答えが一致しているか確認

    print(f"Test: {test}")

