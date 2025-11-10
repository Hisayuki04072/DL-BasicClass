from pathlib import Path

if __name__ == "__main__":
    data_dir = "Lecture4/exercise/data"
    dir_path = Path(data_dir).resolve()
    print("===== problem1 =====")
    print(dir_path)

    print("===== problem2 =====")
    dir_list = list(Path(data_dir).glob("*"))
    for dir in enumerate(dir_list):
        print(dir[1])

    print("===== problem3 =====")
    file_list = list(Path(data_dir).glob("**/*.png"))
    print(len(file_list))