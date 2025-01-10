# Open the file and read using 'with'
def read_data(input_file):
    with open(input_file, 'r') as file:
        return file.read()
   
