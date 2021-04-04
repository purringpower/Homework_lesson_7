number_one = (input("Input number :"))
math_operation = input('Math operation:')
number_two = (input("Input number two:"))


def calculate(number_one, math_operator, number_two):
    if not number_one.isalpha() and not math_operation.isalpha() and not number_two.isalpha():
        if math_operation == '+':
            print('{} + {} = {}'.format(number_one, number_two, int(number_one) + int(number_two)))
        elif math_operation == '-':
            print('{} - {} = {}'.format(number_one, number_two, int(number_one) - int(number_two)))
        elif math_operation == '*':
            print('{} * {} = {}'.format(number_one, number_two, int(number_one) * int(number_two)))
        elif math_operation == '/':
            print('{} / {} = {}'.format(number_one, number_two, int(number_one) / int(number_two)))
        elif math_operation == '//':
            print('{} // {} = {}'.format(number_one, number_two, int(number_one) // int(number_two)))
        elif math_operation == '**':
            print('{} ** {} = {}'.format(number_one, number_two, int(number_one) ** int(number_two)))
        else:
            print('Your operator is not valid!')
    else:
        print('Enter a correct calculation >:C')


calculate(number_one, math_operation, number_two)