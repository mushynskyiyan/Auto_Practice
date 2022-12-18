import string


def check_for_validity(u_inpt):
    if u_inpt[0:2].isalpha() and u_inpt[2:6].isdigit() and u_inpt[6:8].isalpha():
        return True
    else:
        return False


def check_for_length(usr_npt):
    if len(usr_npt) == 8:
        return True
    else:
        return False


def check_for_intersections_in_list(usr_npt, lst):
    chk_var = usr_npt.upper()
    if chk_var in lst:
        print("Value is found in plates list")
        if lst.count(chk_var) > 1:
            return f"This value is not unique in list, found  {lst.count(chk_var)} times in list."
        else:
            return f"This value is unique in list, only {lst.count(chk_var)} time found in list"
    else:
        return f'Value {usr_npt} is not in list'


def sum_of_digits(usr_input):
    lst = []
    for i in range(len(usr_input)):
        if usr_input[i] in string.digits:
            lst.append(int(usr_input[i]))
    sum_of_nums_is_code = 0
    for i in range(len(lst)):
        sum_of_nums_is_code = sum_of_nums_is_code + lst[i]
    return sum_of_nums_is_code


def six_tuple(usr_i):
    tpl = [usr_i[0:2], int(usr_i[2]), int(usr_i[3]), int(usr_i[4]), int(usr_i[5]), usr_i[6:8]]
    return tuple(tpl)


with open("List.json", "r") as f:
    lst_one = f.read()
user_input = input("Enter code: ")

if check_for_length(user_input):
    if check_for_validity(user_input):
        print(f'Congrats, the code is {check_for_validity(user_input)} and valid')
        print(check_for_intersections_in_list(user_input, lst_one))
        print(f'Sum of digits in code: {sum_of_digits(user_input)}')
        print(f'Numbers and letters from code: {six_tuple(user_input)}')
    else:
        print(f'Validity of your code is {check_for_validity(user_input)}')
        print(f'You might be interested in sum of digits in your wrong code,'
              f'so here it is: {sum_of_digits(user_input)}')
else:
    print(f'Sorry, you entered wrong code')
    print(f'You might be interested in sum of digits in your wrong code,'
          f'so here it is: {sum_of_digits(user_input)}')


