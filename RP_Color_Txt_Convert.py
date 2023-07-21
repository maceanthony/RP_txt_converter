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
        '&x': '[/color][color=#000000]', #black
        '&z': '[/color][color=#808080]', #dgrey
        '&w': '[/color][color=#C0C0C0]', #grey
        '&W': '[/color][color=#FFFFFF]', #white
        '&P': '[/color][color=#FF00FF]', #pink
        '&V': '[/color][color=#AF5FAF]', #violet blue
        '&R': '[/color][color=#FF0000]', #red
        '&v': '[/color][color=#AF005F]', #dark magenta
        '&p': '[/color][color=#800080]', #dark pink
        '&r': '[/color][color=#800000]', #red
        '&o': '[/color][color=#AF5F00]', #brown
        '&O': '[/color][color=#FFAF00]', #orange
        '&y': '[/color][color=#AFAF00]', #gold
        '&Y': '[/color][color=#FFFF00]', #yellow
        '&g': '[/color][color=#008000]', #dgreen
        '&n': '[/color][color=#5FAF00]', #chartreuse
        '&G': '[/color][color=#00FF00]', #green
        '&N': '[/color][color=#00FFAF]', #aqua
        '&C': '[/color][color=#00FFFF]', #cyan
        '&c': '[/color][color=#008080]', #dcyan
        '&h': '[/color][color=#008787]', #cadet blue
        '&H': '[/color][color=#5F87FF]', #cornflower blue
        '&b': '[/color][color=#0000FF]', #dark blue
        '&B': '[/color][color=#0000AF]', #even darker blue
    }

    # Replace the color code sequences
    for code, color in color_codes.items():
        content = content.replace(code, color)

    # Write the modified content back to the file
    with open(filename, 'w', encoding='utf-8-sig') as file:
        file.write(content)

    updated_content = content.replace("[/color]", "", 1)

    with open(filename, 'w') as file:
        file.write(updated_content)

    with open(filename, 'a') as file:
        file.write('[/color]')

    print(f"Color codes have been converted in the file: {filename}")


# Call the function to perform the conversion
convert_color_codes()

input("Press enter to exit;")