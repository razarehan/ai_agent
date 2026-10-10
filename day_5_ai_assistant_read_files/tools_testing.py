from tools import read_file

file_path = "./data/shopping_list.txt"

file_content = read_file(file_path)
print(f"Content of '{file_path}':\n{file_content}")