# progIng(Fprog)

def f(x):
    return lambda a: x + a


print(
    f(
        int(
            input()
        )
    )(
        int(
            input()
        )
    )
)


def f2(x, a=0):
    return x + a


def f1(x, f2):

    return x + f2(x)


print(
    f1(
        int(
            input()
        ),
        f2
    )
)
