def calcfn(val1,val2,operation):
    if(operation.upper() == '+' or operation.upper() == 'ADD'):
        return val1+val2;
    elif(operation.upper()=='-'  or operation.upper()== 'MINUS'):
        return val1-val2;
    elif(operation.upper() == '/' or operation.upper() == 'DIVIDE'):
        return val1/val2;
    elif(operation.upper() == '*' or operation.upper() == 'MULTIPLY'):
        return val1*val2;
    else:
        return 'Invalid operator. Please check..'

try:
    val1 = float(input('Enter first number  :  '))
    val2 = float(input('Enter second number  :  '))
    operation = (input('Enter the operation you want to perform (ADD | MINUS | DIVIDE | MULTIPLY |  + - / * ) : '));
    try:
        result = calcfn(val1,val2,operation)
        print('result : ',result)
    except : 
        print('You can\'t divide a number by 0. Please try again..')
except:
    print('Invalid format')
    # good code , but make it even better.


