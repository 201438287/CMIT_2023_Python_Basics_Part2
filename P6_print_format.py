a=1
b=2.34
c=-2023.23456789
print('a = %2d, b=%f, c=%.2f' % (a,b,c), 'CASE 1 (matlab like)\n')
print('a = {:2d}, b={:f}, c={:.2f}'.format(a,b,c), 'CASE 2\n')
print(f'a = {a:2d}, b={b:f}, c={c:.2f}'.format(a,b,c), 'CASE 3\n')
print(f'a = { a}, b={b}, c={c:.2f}   Case 4 lazy\n')
print('a=', a, 'b=',b, 'c', c, 'Case 5 (No format)\n')

