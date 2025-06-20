def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found Please check the path."
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    path = input("Enter the file path: ")
    result = count_lines_of_code(path)
    print(f"gNumber of lines in the file: {result}")