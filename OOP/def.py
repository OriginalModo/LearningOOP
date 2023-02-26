def calc(numbers):
    i  = 0
    for n in numbers:
        i += int(n)
    return i

def test():
    # print('HI')
    return ('HI')


def main():
    numbers = input('Введите числа через запятую: ')
    list_numbers = numbers.split(', ')
    result = calc(list_numbers)
    print(result)
    my_test = test()
    print(my_test)

if __name__ == '__main__':
    main()