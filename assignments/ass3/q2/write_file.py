def save_results(data, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

    
    
def display_results(data):
       for context in data:
              print(context)