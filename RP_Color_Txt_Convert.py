import os
import re

def convert_color_codes():
    # Get the list of files in the current working directory
    files = os.listdir()

    # Filter the files to only include text files
    text_files = [file for file in files if file.endswith('.txt')]

    if len(text_files) == 0:
        print("No text files found in the current directory.")
        return

    # Prompt the user to choose a file
    print("!!!WARNING!!! This will overwrite your current file irreversibly.")
    print("Text files found in the current directory:")
    for i, file in enumerate(text_files):
        print(f"{i+1}. {file}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to the file you want to convert: "))
            if choice < 1 or choice > len(text_files):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    global filename
    filename = text_files[choice - 1]

    # Read the content of the chosen text file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the color code mappings
    color_codes = {
        '&x': '[/color][color=#000000]',
        '&r': '[/color][color=#800000]',
        '&g': '[/color][color=#008000]',
        '&O': '[/color][color=#808000]',
        '&b': '[/color][color=#1A1AFA]',
        '&p': '[/color][color=#800080]',
        '&c': '[/color][color=#008080]',
        '&w': '[/color][color=#C0C0C0]',
        '&z': '[/color][color=#808080]',
        '&R': '[/color][color=#FF0000]',
        '&G': '[/color][color=#00FF00]',
        '&Y': '[/color][color=#FFFF00]',
        '&B': '[/color][color=#0042FF]',
        '&P': '[/color][color=#FF00FF]',
        '&C': '[/color][color=#00FFFF]',
        '&W': '[/color][color=#FFFFFF]'
    }

    # Replace the color code sequences
    for code, color in color_codes.items():
        content = content.replace(code, color)

    # Write the modified content back to the file
    with open(filename, 'w', encoding='utf-8-sig') as file:
        file.write(content)

    with open(filename, 'a') as file:
        file.write('[/color]')

    updated_content = content.replace("[/color]", "", 1)

    with open(filename, 'w') as file:
        file.write(updated_content)


    print(f"Color codes have been converted in the file: {filename}")


# Call the function to perform the conversion
convert_color_codes()

input("Press enter to exit;")