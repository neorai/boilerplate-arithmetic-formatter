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
        
def arithmetic_arranger(problems_list, display_result = False):
    dic_problems = list_to_dic(problems_list)
    error        = check_sintax_errors(problems_list, dic_problems)
    if error: return error
    
    arranged_problems = ""
    first_row  = ""
    second_row = ""
    third_row  = ""
    fourth_row = "" 
    counter = 0
    
    for key, value in dic_problems.items():
        len_value0 = len(value[0])
        len_value2 = len(value[2])
        len_dic_problems = len(dic_problems)
        
        bigger_len_value = len_value0 if len_value0 >= len_value2 else len_value2
        dashes       = "-" * (abs(bigger_len_value) + 2)
        break_line   = "\n" if counter == (len_dic_problems -1) else "    "
        break_result = ""   if counter == (len_dic_problems -1) else "    "
        break_dash   = ""   if counter == (len_dic_problems -1) else "    "
        
        if display_result:
            if value[1] == "+":
                result = int(value[0]) + int(value[2])
            if value[1] == "-":
                result = int(value[0]) - int(value[2])
                
            len_spc        = (abs(bigger_len_value) + 2) - len(str(result))
            spc_fourth_row = " " * len_spc
            fourth_row     += spc_fourth_row + str(result) + break_result
            break_dash     = "\n" if counter ==  (len_dic_problems -1)  else "    "
                       
        if int(value[0]) >= int(value[2]):
            spc_first_row  = 2
            spc_second_row = abs(len_value0 - len_value2)
        else:    
            spc_first_row  = abs(len_value0 - len_value2) + 2
            spc_second_row = 0

        r_aling_first_row  = " " * spc_first_row
        r_aling_second_row = " " * spc_second_row

        first_row  += r_aling_first_row + value[0] + break_line
        second_row += value[1]          + " "      + r_aling_second_row + value[2] + break_line
        third_row  += dashes            + break_dash
       
        counter += 1

    arranged_problems = first_row + second_row + third_row + fourth_row
        
    return arranged_problems

print(arithmetic_arranger(['3401 - 2', '123 + 49']))