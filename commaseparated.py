'''
This code formats a number into the Indian currency style by placing commas according to the Indian numbering system. It separates the last three digits, 
then adds commas every two digits from the right in the remaining part. It also preserves decimal values and works for both integers and floating-point numbers.
'''
def convert_indian_money(n):
    n= str(n)
    if '.' in n:
        int_part, deci_part = n.split('.')
        deci_part = '.' + deci_part
    else:
        int_part = n
        deci_part = ''
    rev = int_part[::-1]
    result = rev[:3]
    for i in range(3, len(rev), 2):
        result += ',' + rev[i:i+2]
    indian_format = result[::-1] + deci_part
    return indian_format

n=float(input())
c=convert_indian_money(n)
print(c)
