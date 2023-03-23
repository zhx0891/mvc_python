def give_me_exp(strn):
    operations = ["+", "-", "*", "/"]
    str_spl = strn.split()
    if len(str_spl) != 3:
        return "не корректное выражение"
    if str_spl[1] in operations:
        if str_spl[0].isdigit() and str_spl[2].isdigit():
            return model.calc_it(str_spl[0], str_spl[1], str_spl[2])

        else:
            return "не кореектные переменные"
    else:
        return "не корректная операция"
        




