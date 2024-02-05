def file_handling_example(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        with open(file_path, 'w') as write_file:
            write_file.write("Trying to write.")

        with open(file_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    raise EOFError("EOF")

    except (FileNotFoundError, PermissionError, EOFError) as e:
        print(e)

file_handling_example('1.txt')
