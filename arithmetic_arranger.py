import re
def list_to_dic(problems_list):
    counter = 0
    dic_problems = {}
    for problem in problems_list:
        problem_split = problem.split()
        dic_problems[counter] = problem_split
        counter += 1
    return dic_problems

def check_sintax_errors(problems_list, dic_problems):
    if len(problems_list) > 5:
        return "Error: Too many problems."
        
    for key, value in dic_problems.items():
        if value[1] != "+" and value[1] != "-":
            return "Error: Operator must be '+' or '-'."
        elif value[0].isnumeric() == False or value[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        elif len(value[0]) > 4 or len(value[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
'''def space_break(row, dic_problems):

def right_aligned(dic_problems, display_result):
    for key, value in dic_problems.items():'''
        
def arithmetic_arranger(problems_list, display_result = False):
    dic_problems = list_to_dic(problems_list)
    error = check_sintax_errors(problems_list, dic_problems)
    if error: return error
    
    arranged_problems = ""
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = "" 
    counter = 0
    for key, value in dic_problems.items():
        bigger_len_value = len(value[0]) if len(value[0]) >= len(value[2]) else len(value[2])
        line_break = "\n" if counter == (len(dic_problems) -1) else "    "
        break_result = "" if counter == (len(dic_problems) -1) else "    "
        dashes = "-" * (abs(bigger_len_value) + 2)
        break_dash = "" if counter == (len(dic_problems) -1)  else "    "
        
        if display_result:
            if value[1] == "+":
                result = int(value[0]) + int(value[2])
            if value[1] == "-":
                result = int(value[0]) - int(value[2])
            len_white_spc_fourth_row = (abs(bigger_len_value) + 2) - len(str(result))
            white_spc_fourth_row = " " * len_white_spc_fourth_row
            fourth_row = fourth_row + white_spc_fourth_row + str(result) + break_result
            break_dash = "\n" if counter ==  (len(dic_problems) -1)  else "    "
                       
        if int(value[0]) >= int(value[2]):
            r_aling_first_row = 2
            r_aling_second_row = abs(len(value[0]) - len(value[2]))
        else:    
            r_aling_first_row = abs(len(value[0]) - len(value[2])) + 2
            r_aling_second_row = 0

        white_spc_first_row = " " * r_aling_first_row
        white_spc_second_row = " " * r_aling_second_row

        first_row = first_row + white_spc_first_row + value[0] + line_break
        second_row = second_row + value[1] + " " + white_spc_second_row + value[2] + line_break
        third_row = third_row + dashes + break_dash
       
        counter += 1

    arranged_problems = first_row + second_row + third_row + fourth_row
        
    return arranged_problems

print(arithmetic_arranger(['3401 - 2', '123 + 49']))