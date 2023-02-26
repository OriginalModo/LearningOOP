# def func():
#     pass
#
# func()


# def my_name(name):
#     print(name)
#
# my_name("John")


# def calc(a=5, b=5):
#     c = a + b
#     return c
#
# result = calc()
# print(result)


# def my_func(*args):
#     print(args)
#     print(type(args))
#
# my_test_list = [1, 2, 3, 'HI', 5]
# my_func(my_test_list)


# def my_func2(*args,**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print(args)
#     print(type(args))
#
# my_test_dict = {'key':1, 'word':"Hi", 'number':5}
# my_func2(my_test_dict)


def my_func3(b ,**kwargs):
    # print(a)
    print(b)
    # print(args)
    print(kwargs)


my_func3('test', key=1, key2=44)