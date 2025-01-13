from importlib.resources import contents


def merge_files(file1, file2, output_file):
    """
    Merges the contents of two files into a third file.

    Args:
        file1 (str): Path to the first input file.
        file2 (str): Path to the second input file.
        output_file (str): Path to the output file.

    Returns:
        str: Success message or error encountered.
    """
    try:
        data = ""

        # Read first file
        with open(file1, 'r') as fp:
            data = fp.read()

        # Read second file
        with open(file2, 'r') as fp:
            data2 = fp.read()

        # Combine contents
        data += "\n" + data2

        # Write to the output file
        with open(output_file, 'w') as fp:
            fp.write(data)

        return f"Files '{file1}' and '{file2}' successfully merged into '{output_file}'."

    except FileNotFoundError as e:
        return f"Error: {e.filename} not found."

    except IOError as e:
        return f"Error: An I/O error occurred - {str(e)}."

file1 = 'sample.txt'
file2 = 'sample2.txt'
output_file = 'file3.txt'

result = merge_files(file1, file2, output_file)
print(result)

with open("file3.txt",'r') as ansh:
    contents=ansh.read()
    print(contents)

