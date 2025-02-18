def calculate(num1,num2,operator):
    operator_list = ['+','-','*','/']
    if operator in operator_list:
        if operator == '+':
            return f'num1 + num2 = {num1 + num2}'
        elif operator == '-':
            return f'num1 - num2 = {num1 - num2}'
        elif operator == '*':
            return f'num1 * num2 = {num1 * num2}'
        else:
            try:
                if num2 != 0:
                    return f'num1 / num2 = {num1 / num2}'
                else:
                    raise ValueError('Invalid : number cannot divided by 0')
            except ValueError as e:
                return str(e)
    else:
        return f"Operator mutbe one of them ['+','-','*','/'] "

print(calculate(3,0,' '))
print(calculate(3,10,'+'))
print(calculate(3,10,'/'))
print(calculate(3,10,'-'))


 



