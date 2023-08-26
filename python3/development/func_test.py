def apply(*args):
    output = None
    *func, data = args
    try:
        output = func[0](data)
    except Exception:
        output = apply(*args[1:])
    finally:
        return output

print(apply(lambda x: 1/x, lambda x: x, 2))
