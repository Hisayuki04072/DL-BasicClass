from utils.count import count_word

if __name__ == "__main__":
    s = "hello world"
    print("e:", count_word(s, "e")) # 1
    print("o:", count_word(s, "o")) # 2
    print("l:", count_word(s, "l")) # 3
    count_word(s, "aaa")

    


