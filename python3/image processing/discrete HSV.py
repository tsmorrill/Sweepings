from functools import reduce

TITLE = 'discrete_HSV.py'
AUTHOR = 'The Overboard Partitioner'
VERSION = '0.2'

# v0.2
# - implemented forwards map

DESCRIPTION = (
    'An integer-based RGB <-> HSV mapping by Chernov, Alander, and Bochko.')

# "Integer-based accurate conversion between RGB and HSV color spaces."
# Vladimir Chernov, Jarmo Alander, Vladimir Bochko; 2015

MODES = ['RGB -> HSV', 'HSV -> RGB']

def compose(*funcs):
    if funcs == ():
        chain = lambda x: x
    else:
        head, *tail = funcs
        chain_t = compose(*tail)
        chain = lambda x: head(chain_t(x))
    return lambda x: chain(x)


def welcome():
    print(f'{AUTHOR} welcomes you to {TITLE}.')
    print('')
    print(DESCRIPTION)
    print('')
    print(f'(v{VERSION})')
    print('')
    

def oops():
    print('Come again?')
    print('')


def pick(options:tuple, msg="Here's what we can do:"):
    if msg != '':
        print(msg)
    verbose = (f'    {i}: {opt}' for i, opt in enumerate(options))
    for line in verbose:
        print(line)
    print('')
    selection = None
    while selection is None:
        try:
            i = int(input("What'll it be?\n"))
            selection = options[i]
        except:
            oops()
    print('')
    return selection


def prompt(msg:str, mode:str):
    command = input(msg)
    seq = tuple(int(val) for val in command.split())
    print('')
    bar = b_string(seq)
    print(f"That's {bar}.")
    print('')
    options = tuple(p_seq(seq) for _ in range(4))
    bars = tuple(b_string(opt) for opt in options)
    return bars


def sector(data:tuple, m:int, M:int):
    match data:
        # double check the assignment syntax
        case M, _, m:
            i = 0
        case _, M, m:
            i = 1
        case m, M, _:
            i = 2
        case m, _, M:
            i = 3
        case _, m, M:
            i = 4
        case M, m, _:
            i = 5
    return i


def hue(data:tuple, m:int, c:int, M:int):
    if m == M:
        h = None
    else:
        E = 65537
        i = sector(data, m, M)
        f = (c - m) << 16
        f //= 16
        f += 1
        if i % 2 == 1:
            f = E - f
        h = E*i + f
    return h


def sat(data:tuple, m:int, M:int):
    d = M - m
    if d == 0:
        s = 0
    else:
        s = (d << 16) - 1
        s //= M
    return s


def hsv(data:tuple):
    m, c, M = sorted(data)
    return hue(data, m, c, M), sat(data, m, M), M


def red(data:tuple):
    pass


def blu(data:tuple):
    pass


def grn(data:tuple):
    pass


def rgb(data:tuple):
    return red(data), blu(data), grn(data)


def report(output:tuple, mode:str):
    print('')
    print(output)


def ciao():
    print('Ciao!')


def main():
    welcome()
    mode = pick(MODES)
    msg = {'RGB -> HSV':(
        'Enter an RBG triple separated by spaces. Values 0-255, please.\n'),
           'HSV -> RGB':(
        'Enter an HSV triple separated by spaces.\n')}
    command = input(msg[mode])
    data = tuple(int(val) for val in command.split())
    action = {'RGB -> HSV':hsv,
              'HSV -> RGB':rgb}
    output = action[mode](data)
    report(output, mode)
    ciao()


if __name__ == '__main__':
    main()
