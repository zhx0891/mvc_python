import controller


def just_do_it():
    print("Это калькулятор!  Введите простое выражение типа  a + b \n"
          "из целых чисел, доступны сложение, вычитание, произведение и разность.")
    exp = input()
    print(controller.give_me_exp(exp))


just_do_it()

