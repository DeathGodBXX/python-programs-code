def PReven(n):
    start = 1
    while start <= n:
        if start % 2 == 0:
            yield start
        start = start + 1
    return 'Finished'


i = 1
even = PReven(100)
while True:
    try:
        print(next(even), end=',')
        if i % 10 == 0:
            print()
        i = i + 1
    except Exception as e:
        print(e)
        break
