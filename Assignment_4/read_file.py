try:
    print("Reading file content:")
    with open('Assignment_4/sample.txt', 'r') as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")