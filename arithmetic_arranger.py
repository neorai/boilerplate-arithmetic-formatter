import re

def arithmetic_arranger(problems_list, display = False):
    arranged_problems = 0
    
    #Check len of list         
    if len(problems_list) > 5:
        return "Error: Too many problems."
    
    #Check Operators 
    dic_problems = {}
    cont = 0
    for problem in problems_list:
        problem_split = problem.split()
        dic_problems[cont] = problem_split
        cont += 1
        
    for key, value in dic_problems.items():
        if value[1] != "+" and value[1] != "-":
            return "Error: Operator must be '+' or '-'."
        elif value[0].isnumeric() == False or value[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."
        elif len(value[0]) > 4 or len(value[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
    return "ok"

print(arithmetic_arranger(["32 + 698", "3401 - 2", "45 + 43", "123 + 49"]))