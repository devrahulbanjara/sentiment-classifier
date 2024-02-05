def file_handling_example(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        with open(file_path, 'w') as write_file:
            write_file.write("Trying to write.")

        with open(file_path, 'r') as eof_file:
            while eof_file.read(1024):
                pass

    except (FileNotFoundError, PermissionError, EOFError) as e:
        print(e)

file_handling_example('your_file_path/your_file.txt')
