j = 1
print('*' * 110)
while j <= 9:
    i = 1
    while i <= j:
        s = j * i
        # print('%s*%s=%s' % (j, i, j * i), end='\t')  #%s指定匹配string型，%d指定匹配整形，%f指定匹配浮点型
        # print(f'{j}*{i}={j * i}', end='\t')  # 利用f匹配表达式,并用大括号括起来
        # print(j, '*', i, '=', (j * i), end='\t')
        print('{}*{}={}'.format(j, i, j * i), end='\t')
        i = i + 1
    print()
    j = j + 1
print('*' * 110)
