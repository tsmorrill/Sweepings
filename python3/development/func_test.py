def apply(*args):
    output = None
    *func, data = args
    try:
        output = func[0](data)
    except Exception:
        output = apply(*args[1:])
    finally:
        return output


def comp_test(*funcs):
    if funcs == ():
        print('bingo')
    print(funcs)


comp_test()
