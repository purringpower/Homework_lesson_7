limit_number = int(input('enter the limit number:'))


def count_to_the_limit(limit_number):
    for i in range(1, limit_number):
        if i % 2 == 0:
            print(i, '- even number')
        else:
            print(i, '- odd number')


count_to_the_limit(limit_number)