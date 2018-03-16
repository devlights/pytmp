

def add(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    import functools as ft
    import timeit as ti

    p = ft.partial(add, 3)
    b = add.__get__(3)

    t1 = ti.timeit('p(3)', globals=locals())
    t2 = ti.timeit('b(3)', globals=locals())

    print(f'{round(t1, 2)}\n{round(t2, 2)}')
