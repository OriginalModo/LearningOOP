def func():
    play_list = ['1', '2', 'sound3', 'sound4', 'sound5']
    # play_list = ['1', '2']
    ints = []
    try:
        for line in play_list:
            ints.append(int(line))
    except ValueError:
        print('Это не число')
    # except Exception:
    #     print('Что-то пошло не так')
    else:
        print('Все хорошо')
    finally:
        print(ints)

func()