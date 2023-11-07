import re


def list_to_dic(list_problems):
    counter = 0
    dic_problems = {}
    for problem in list_problems:
        problem_split = problem.split()
        dic_problems[counter] = problem_split
        counter += 1
    return dic_problems


def check_sintax_errors(list_problems, dic_problems):
    if len(list_problems) > 5:
        return "Error: Too many problems."

    for key, value in dic_problems.items():
        if value[1] != "+" and value[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if value[0].isnumeric() is False or value[2].isnumeric() is False:
            return "Error: Numbers must only contain digits."
        if len(value[0]) > 4 or len(value[2]) > 4:
            return "Error: Numbers cannot be more than four digits."


def arithmetic_arranger(list_problems, display_result=False):
    dic_problems = list_to_dic(list_problems)
    error = check_sintax_errors(list_problems, dic_problems)
    if error:
        return error

    arranged_problems = ""
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""

    for key, value in dic_problems.items():
        int_value0 = int(value[0])
        int_value2 = int(value[2])

        if value[1] == "+":
            result = int_value0 + int_value2
        else:
            result = int_value0 - int_value2

        num_list = [int(len(value[0])), int(len(value[2]))]
        num_max = max(num_list) + 2
        dashes = "-" * num_max

        if key == (len(dic_problems) - 1):
            white_space = ""
        else:
            white_space = "    "

        first_row += str(value[0]).rjust(num_max) + white_space
        second_row += value[1] + str(value[2]).rjust(num_max - 1) + white_space
        third_row += dashes + white_space
        fourth_row += str(result).rjust(num_max) + white_space

    if display_result:
        arranged_problems = (
            first_row + "\n" + second_row + "\n" + third_row + "\n" + fourth_row
        )
    else:
        arranged_problems = first_row + "\n" + second_row + "\n" + third_row

    return arranged_problems


print(arithmetic_arranger(["3401 - 2", "123 + 49"], True))
