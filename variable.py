'''
Arithmetic Operator
=========================
+   addition
-   subtraction
*   multiplication
/   division
%   remainder
//  integer division
**  exponent

exception handling
=======================
try:
    statement1
    ...
except:
    statement2
    ...    
'''

try:
    x=input('enter value for X : ')
    x=float(x)
    y=float(input('enter value for Y : '))


    print(f'the addition is : {x+y}')
    print(f'the subtraction is : {x-y}')
    print(f'the multiplication is : {x*y}')
    print(f'the division is : {x/y}')
    print(f'the integer division is : {x//y}')
    print(f'the remainder is : {x%y}')
    print(f'the exponent is : {x**y}')
except Exception as ex:
    pass
    # print(ex)
