def make_pretty(func):
    def inner():
        print('ya tupoi')
        func()
    return inner

@make_pretty
def ordinary():
    print('ya ochen tupoi')


ordinary()
# petty = make_pretty(ordinary)
# petty()


