run = True
def calculate(num1, sign, num2):
    num1 = int(num1)
    num2 = int(num2)
    sign = str(sign)
    if sign == '+':
        print(num1 + num2)
    if sign == '/':
        print(num1 / num2)
    if sign == '*':
        print(num1 * num2)
    if sign == '-':
        print(num1 - num2)

print('to use this write you problem like this 1 + 1, it very\nimportant that the spaces are put correctly\nto quit type quit\nAlso for now only small equations can be done [1 + 1,3 * 4...]')

while run:
    n1, sig, n2 = input('>>').split()
    if n1 == 'quit':
        run = False
    else:
        calculate(n1, sig, n2)