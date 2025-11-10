from pathlib import Path

def get_files_in_directory(data_directory):
    assert (data_directory.exists() and data_directory.is_dir()),  "'data' directory not found."

    file_list = list(data_directory.glob("*"))

    return file_list

def check_file_existence(file_path):
    path = Path(file_path)
    if path.exists():
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")


if __name__ == "__main__":
    data_directory = "Lecture4/example/data"
    data_directory_path = Path(data_directory).resolve()
    print("---absolute path---")
    print(data_directory_path)

    files_in_data = get_files_in_directory(data_directory_path)
    print("---all files underneath---")
    for file in files_in_data:
        print(file)

    base_directory = Path("/base_dir")
    subdirectory_name = "data_dir"

    new_path = base_directory / subdirectory_name
    print("---concatenate path---")
    print(new_path)    

    # directory_path = Path("./target_dir")
    # directory_path.mkdir(parents=True, exist_ok=True)