filename = input("Enter the filename you want to read: ")

try:
    with open(filename, 'r') as file:  # Use the actual input from the user
        content = file.readlines()

    modified_content = []

    for line in content:
        modified_line = line.strip() + " - Modified"
        modified_content.append(modified_line)

    new_filename = 'modified_' + filename
    with open(new_filename, 'w') as file:
        for line in modified_content:
            file.write(line + '\n')

    print(f"✅ File has been modified and saved as '{new_filename}'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")

except IOError:
    print(f"❌ Error: Could not read the file '{filename}'.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
