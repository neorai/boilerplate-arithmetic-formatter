import re

def arithmetic_arranger(problems_list, display = False):
    arranged_problems = ""
    dic_problems = {}
    first_row = ""
    second_row = ""
    dashes_row = ""
    result_row = ""
    #Error handling       
    if len(problems_list) > 5:
        return "Error: Too many problems."
    
    counter = 0 
    for problem in problems_list:
        problem_split = problem.split()
        dic_problems[counter] = problem_split
        counter += 1
        
    for key, value in dic_problems.items():
        if value[1] != "+" and value[1] != "-":
            return "Error: Operator must be '+' or '-'."
        elif value[0].isnumeric() == False or value[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        elif len(value[0]) > 4 or len(value[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    counter = 0
    for key, value in dic_problems.items():
        bigger_len_value = len(value[0]) if len(value[0]) >= len(value[2]) else len(value[2])
        line_break = "\n" if counter == (len(dic_problems) -1) else "    "
        line_break_result = "" if counter == (len(dic_problems) -1) else "    "
        dashes = "-" * (abs(bigger_len_value) + 2)
        line_break_dash = "" if counter == (len(dic_problems) -1)  else "    "
        
        if display:
            if value[1] == "+":
                result = int(value[0]) + int(value[2])
            if value[1] == "-":
                result = int(value[0]) - int(value[2])
            len_white_spc_result_row = (abs(bigger_len_value) + 2) - len(str(result))
            white_spc_result_row = " " * len_white_spc_result_row
            result_row = result_row + white_spc_result_row + str(result) + line_break_result
            line_break_dash = "\n" if counter ==  (len(dic_problems) -1)  else "    "
                       
        if int(value[0]) >= int(value[2]):
            len_white_spc_first_row = 2
            len_white_spc_second_row = abs(len(value[0]) - len(value[2]))
        else:    
            len_white_spc_first_row = abs(len(value[0]) - len(value[2])) + 2
            len_white_spc_second_row = 0

        white_spc_first_row = " " * len_white_spc_first_row
        white_spc_second_row = " " * len_white_spc_second_row

        first_row = first_row + white_spc_first_row + value[0] + line_break
        second_row = second_row + value[1] + " " + white_spc_second_row + value[2] + line_break
        dashes_row = dashes_row + dashes + line_break_dash
       
        counter += 1

    arranged_problems = first_row + second_row + dashes_row + result_row
        
    return arranged_problems

print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))