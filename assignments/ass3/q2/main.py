from assignments.FunctionandModules.q2.read_data import read_data
from assignments.FunctionandModules.q2.write_file import save_results, display_results
from assignments.FunctionandModules.q2.process_data import filter_data


def main():
    input_file='example.txt'
    output_file='output.txt'
    keyword='harvey'
    data=read_data(input_file)

    processed_data=filter_data(data,keyword)
    save_results(processed_data,output_file)
    display_results(processed_data)

if __name__ == '__main__':
    main()