# Assignment_4
For Task 1, firstly print line just prints a message on the screen that says "Reading file content:" to ensure that it matches with expected output. with open('sample.txt', 'r') as file: This line tries to open a file named sample.txt in read mode ('r' stands for read). If the file exists, it will be opened, and the content can be read. The with statement ensures that the file is properly closed after the program finishes working with it, even if an error occurs.
for i, line in enumerate(file, start=1): This line reads the file line by line. The enumerate(file, start=1) part gives each line a number, starting from 1. For example, it reads the first line and gives it the number 1, the second line gets 2, and so on.
print(f"Line {i}: {line}", end=''): This line prints the current line number and the content of that line in the file. i is the line number, and line is the actual content of that line. The end='' part ensures that there is no extra new line between each print statement (since line already contains the new line character).
except FileNotFoundError: This is the "except" block. If there’s an error when trying to open the file (for example, if the file doesn't exist), it will catch that specific error (FileNotFoundError).print("Error: The file 'sample.txt' does not exist."). If the file is not found, it will print an error message: "The file 'sample.txt' does not exist."


For task 2, file1=open('output.txt','w') This line opens a file named output.txt in write mode ('w'). If the file doesn't exist, it will be created. If it already exists, it will be overwritten.
writing = file1.write(input("Enter text to write to the file: ")): The code prompts the user to enter some text using the input() function. Whatever the user types is written to output.txt using the write() method.The input() function waits for the user to type something, and the write() method then writes that input into the file.
print("Data successfully written to output.txt"): After the user’s input is written to the file, this message is printed to let the user know that the text was successfully saved.
file1=open('output.txt','a'): This line reopens the same output.txt file, but this time in append mode ('a'). This means any new text will be added to the end of the file without overwriting the existing content.
appending = file1.write(input("Enter additional text to append: "))
Similar to the previous step, the program prompts the user for more input, which is then added to the end of the file.
print("Data successfully appended")
After appending the new text, this message is printed to inform the user that the additional text was successfully added.
with open('output.txt', 'r') as file1: Now, the program opens the output.txt file in read mode ('r') to check and display the final content of the file. The with statement ensures that the file is automatically closed after reading.
reading = file1.read(): This line reads the entire content of the file and stores it in the reading variable.
print("Final content of output.txt:", reading): Finally, it prints the entire content of the file, showing both the original text and the appended text.
file1.close(): This line explicitly closes the file. It’s a good practice to close files to release resources.
