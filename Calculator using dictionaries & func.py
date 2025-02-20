def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":subtract,"*":multiply,"/":divide,}

# print(operations["*"](4,8))
def calculator():
    stop_calc=False
    first_num = float(input("Enter the first number\n"))
    while not stop_calc:
        for symbol in operations:
            print(symbol)
        operator_chosen=input('Choose operation\n')
        second_num=float(input("Enter the second number\n"))

        for i in operations:
            if operator_chosen==i:
                current_operation_result=operations[i](first_num,second_num)
                print(f"{first_num}{operator_chosen}{second_num}={current_operation_result}")

        you_continue=input("Type 'y' for yes and 'n' for no\n").lower()
        if you_continue=='y':
            first_num=current_operation_result
        else:
            stop_calc=True
            print("\n"*30)
            calculator()   #RECURSION

calculator()
