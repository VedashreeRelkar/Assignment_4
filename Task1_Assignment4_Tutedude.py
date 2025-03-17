print("Reading file content:")
try:
    with open('sample.txt', 'r') as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line}",end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")