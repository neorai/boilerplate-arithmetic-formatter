"""
Correct conversion if the supplied problems are properly formatted, 
otherwise, it will return a string that describes an error that is meaningful to the user.
"""


def list_to_dic(list_problems):
    """
    Converts a list of problems into a dictionary.

    Args:
        list_problems (list): A list of problems in string format.

    Returns:
        dict: A dictionary where the keys are the indices of the problems,
              and the values are lists of strings representing each problem.

    Example:
        >>> problems = ["2 + 2", "5 - 3", "7 * 4"]
        >>> result = list_to_dic(problems)
        >>> print(result)
        {0: ['2', '+', '2'], 1: ['5', '-', '3'], 2: ['7', '*', '4']}
    """
    dic_problems = {}
    for index, problem in enumerate(list_problems):
        problem_split = problem.split()
        dic_problems[index] = problem_split

    return dic_problems


def check_sintax_errors(list_problems, dic_problems):
    """
    Checks for syntax errors in a list of problems.

    Args:
        list_problems (list): A list of problems in string format.
        dic_problems (dict): A dictionary of problems.

    Returns:
        str: An error message if any syntax errors are found, or False if no errors are found.

    Example:
        >>> problems = ["2 + 2", "5 - 3", "7 * 4"]
        >>> dictionary = {0: ['2', '+', '2'], 1: ['5', '-', '3'], 2: ['7', '*', '4']}
        >>> result = check_syntax_errors(problems, dictionary)
        >>> print(result)
        False
    """
    error = False
    if len(list_problems) > 5:
        error = "Error: Too many problems."

    for value in dic_problems.values():
        if value[1] != "+" and value[1] != "-":
            error = "Error: Operator must be '+' or '-'."
        if value[0].isnumeric() is False or value[2].isnumeric() is False:
            error = "Error: Numbers must only contain digits."
        if len(value[0]) > 4 or len(value[2]) > 4:
            error = "Error: Numbers cannot be more than four digits."

    return error


def arithmetic_arranger(list_problems, display_result=False):
    """
    Arrange and optionally display the results of arithmetic problems.

    Args:
        list_problems (list): A list of arithmetic problems in string format.
        display_result (bool, optional): Whether to display the results. Defaults to False.

    Returns:
        str: A formatted string containing the arranged problems and results.

    Example:
        >>> problems = ["2 + 2", "5 - 3", "7 * 4"]
        >>> result = arithmetic_arranger(problems)
        >>> print(result)
           2       5       7
        +  2    -  3    *  4
        ----    ----    ----

        >>> result = arithmetic_arranger(problems, True)
        >>> print(result)
           2       5       7
        +  2    -  3    *  4
        ----    ----    ----
           4       2      28
    """
    dic_problems = list_to_dic(list_problems)
    error = check_sintax_errors(list_problems, dic_problems)
    if error:
        return error

    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""

    for key, value in dic_problems.items():
        if value[1] == "+":
            result = int(value[0]) + int(value[2])
        else:
            result = int(value[0]) - int(value[2])

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


print(arithmetic_arranger(["3403 - 2", "123 + 49"], True))
