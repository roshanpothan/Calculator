#print( "enter the first valu" )
#print" )
#sum= first_value + second_value
#print("adittion is %d", sum)
#sub= first_value - second_value
#print("substarction is %d", sub)
#div= first_value / second_value
#print("division is %d", div)


# def cal(question):
#     sum=0
#     expression=input(question)  
#     operands=expression.split('+')
#     if(expression.isnumeric() == False):
#      print("invalid expression")
#     else:
#      print("valid expression")
# cal("Enter Expression: ")
 #for operand in expression:
 # print(operands)#['99', '665', '565', '3213', '2121', '25']
    # for operand in operands:
    #     sum=sum+int(operand)
    #     print(f"sum= {sum}")


# result=0
# flag=0  
# expression=input("enter expression: ")
# operands=expression.split('+,-')
# for operand in operands:
#     if (operand.isnumeric()==False or operand==''):
#         print("invalid expression")
#         flag=1
#         break
#     if(operand.endswith('+','-') and int(operand) < 0 and (operand==int(operand))):
#         result= result + int(operand)
#     if(flag!=1):
#        print(f"result={result}")
   











# expression_valid=[]
# expression=input("Enter expression: ") #56+96-37-23+89+65-12+69-75
# expression_list=expression.split('+')
# 
import re
expression_valid=[]
expression='(56+78+89-24)-34+56-(23+34+44)+(5+6-8)' #199-34+56-101
expression_bak=expression
expression_list=[]
priority_list=[]
while(expression!=''):
    start=expression.find('(')#0
    stop=expression.find(')')#12
    priority_list.append(expression[start+1:stop]) #0+1:12
    expression=expression[stop+1:]
    print(f'start: {start},stop: {stop}, priority_list: {priority_list},expression:{expression}')

expression=expression_bak

for x in range(len(priority_list)):
    expression=expression.replace(priority_list[x],'').replace('(','').replace(')','')
print(priority_list)
print(expression)
result = 0
for item in priority_list:
    stack=[]
    num =""
for char in item:
    if char.isnumeric():
        num += char
    else:
        if num:
            stack.append(int(num))
            num = ""
            if char in  '+-':
             if char == '+': 
                stack .append(stack.pop() + stack.pop())
            else:
                stack.append(-stack.pop() + stack.pop())
                if num:
                  stack.append(int(num))
                result += stack[0]

                print(result)

    # for number in expression_list:
    #     if(number.isnumeric()):
    #         expression_valid.append(int(number))
    #         print(f"expression_valid={expression_valid}")
    # else:  numbers=number.split('-')
    # expression_valid.append(int(numbers[0]))
           
    # for i in range(1,len(numbers)):
    #         expression_valid.append(int(numbers[i]*(-1)))
    #         print(f"expression_valid={expression_valid}")
   

    #         print(f"total={sum(expression_valid)}")


#  numbers=number.split('-')
#             print(numbers)
#             expression_valid.append(int(numbers[0]))
#             print(f"expression_valid={expression_valid}")
