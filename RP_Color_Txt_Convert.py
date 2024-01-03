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
        '&z': '[/color][color=#808080]',
        '&w': '[/color][color=#C0C0C0]',
        '&W': '[/color][color=#FFFFFF]',
        '&P': '[/color][color=#FF00FF]',
        '&p': '[/color][color=#800080]',
        '&R': '[/color][color=#FF0000]',
        '&r': '[/color][color=#800000]',
        '&O': '[/color][color=#808000]',
        '&Y': '[/color][color=#FFFF00]',
        '&g': '[/color][color=#008000]',
        '&G': '[/color][color=#00FF00]',
        '&C': '[/color][color=#00FFFF]',
        '&c': '[/color][color=#008787]',
        '&B': '[/color][color=#0000FF]',
        '&b': '[/color][color=#0000AF]',
        '}a': '[/color][color=#005FAF]',
        '}A': '[/color][color=#0087FF]',
        '}b': '[/color][color=#5F87FF]',
        '}B': '[/color][color=#5FD7FF]',
        '}c': '[/color][color=#00AFAF]',
        '}C': '[/color][color=#00D7FF]',
        '}e': '[/color][color=#4E4E4E]',
        '}E': '[/color][color=#5F5F5F]',
        '}g': '[/color][color=#00AF00]',
        '}G': '[/color][color=#87FF00]',
        '}j': '[/color][color=#00AF5F]',
        '}J': '[/color][color=#00FF87]',
        '}l': '[/color][color=#5FAF00]',
        '}L': '[/color][color=#87FF00]',
        '}m': '[/color][color=#AF00AF]',
        '}M': '[/color][color=#D700AF]',
        '}o': '[/color][color=#AF5F00]',
        '}G': '[/color][color=#FF8700]',
        '}p': '[/color][color=#AF005F]',
        '}P': '[/color][color=#FF0087]',
        '}r': '[/color][color=#AF0000]',
        '}R': '[/color][color=#D70000]',
        '}s': '[/color][color=#878787]',
        '}S': '[/color][color=#D7D7D7]',
        '}t': '[/color][color=#875F00]',
        '}T': '[/color][color=#D7AF00]',
        '}v': '[/color][color=#5F00AF]',
        '}V': '[/color][color=#8700FF]',
        '}w': '[/color][color=#AFAFAF]',
        '}W': '[/color][color=#DADADA]',
        '}y': '[/color][color=#AFAF00]',
        '}Y': '[/color][color=#FFD700]',

    }

    # Replace the color code sequences
    for code, color in color_codes.items():
        content = content.replace(code, color)

    # Write the modified content back to the file
    with open(filename, 'w', encoding='utf-8-sig') as file:
        file.write(content)

    updated_content = content.replace("[/color]", "", 1)

    with open(filename, 'w', encoding='utf-8-sig') as file:
        file.write(updated_content)

    with open(filename, 'a') as file:
        file.write('[/color]')

    print(f"Color codes have been converted in the file: {filename}")


# Call the function to perform the conversion
convert_color_codes()

input("Press enter to exit;")