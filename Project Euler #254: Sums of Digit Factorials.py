# This program need to be further optimized


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


fact_table = dict()
fn = dict()
sfn = dict()
gi = dict()
sgi = dict()

for i in range(0, 10):
    fact_table[i] = factorial(i)


def f(n):

    global fn
    global M

    if n in fn:
        return fn.get(n)

    result = 0

    for i in str(n):
        result = result + fact_table[int(i)]
        result %= M

    fn[n] = int(result)

    return fn.get(n)



def sf(n):

    global sfn
    global M

    if n in sfn:
        return sfn.get(n)

    result = 0

    for i in str(f(n)):
        result = result + int(i)
        result %= M

    sfn[n] = int(result)

    return sfn.get(n)


def g(i):

    global gi
    global M

    if i in gi:
        return gi.get(i)

    n = 1
    sf_val = sfn.get(n, sf(n))
    while sf_val != i:
        n += 1
        sf_val = sfn.get(n, sf(n))

    gi[i] = int(n)

    return gi.get(i)


# print(g(48))


def sg(i):

    global sgi
    global M

    if i in sgi:
        return sgi.get(i)

    result = 0

    for i in str(g(i)):
        result = result + int(i)
        result %= M

    sgi[i] = int(result)

    return sgi.get(i)


# print(sg(3))

def solve(n):

    global M

    result = 0

    for i in range(1, n + 1):
        result += sg(i)
        result %= M

    return result


for q in range(int(input())):
    N, M = map(int, input().split())

    print(solve(N) % M)
