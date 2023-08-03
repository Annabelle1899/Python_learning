def f(a, b, c):
    print(f"a={a}, b={b}, c={c}")

d = {"a":1, "b":2, "c":3}

l = [4,5,6]
f(*l)

f(**d)