from typing import TextIO, List

file_path = r"data\step2_2.txt"

def calculator (oper: str, a: int, b: int) -> float :

    if oper == '/':
        return a/b
    elif oper == 'x':
        return a*b
    elif oper == '+':
        return a+b
    elif oper == '-':
        return a-b

def got_to_line(lines_list: List, line_number: int) -> TextIO:
    
    return lines_list[line_number]


def execute_command(lines:TextIO, line_inputs: List):

    if line_inputs[0] == 'goto' and (len(line_inputs) > 2):
        line_index = int(calculator(line_inputs[2],int(line_inputs[3]),int(line_inputs[4])))-1
        new_line = got_to_line(lines, line_index)
    else:
        line_index = int(line_inputs[1])-1
        new_line = got_to_line(lines, line_index)

    return new_line, line_index


def compute_file (filepath:str):

    with open(file_path) as f:
        lines= f.readlines()
        lines_check = []
        line_inputs = []
        line = lines[0]
        while line_inputs not in lines_check:
            line_inputs = line.split(' ')
            lines_check.append(line_inputs)
            line, line_index = execute_command(lines, line_inputs)
            line_inputs = line.split(' ')
            
    
    return print(line_inputs, line_index)

if __name__ == '__main__':
    compute_file(file_path)


