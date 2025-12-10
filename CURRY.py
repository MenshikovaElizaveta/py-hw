def sum3(x, y, z):
    return x+y+z


def curry(func, number_of_args):
    if not callable(func):
        raise TypeError("Первый аргумент должен быть функцией")
    if number_of_args < 0:
        raise ValueError("Арность не может быть отрицательной")
    if number_of_args > func.__code__.co_argcount:
        raise ValueError("Переданная функции арность больше, чем по факту")
    def curried(*args):
        if len(args)==number_of_args:
            return func(*args)
        else:
            def moving(next_arg):
                return curried(*args, next_arg)
            return moving
    return curried


def uncurry(func, number_of_args):
    if not callable(func):
        raise TypeError("Первый аргумент должен быть функцией")
    def uncur(*args):
        if len(args) != number_of_args:
           raise ValueError(f"Ожидается {number_of_args} аргументов, получено {len(args)}")
        a=func
        for arg in args:
            a=a(arg)
        return a
    return uncur