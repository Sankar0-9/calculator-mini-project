def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "cannt divide by zero"
    return a/b
def cal():
    while True:
        print("\n======= CALCULAROR MENU =======")
        print("1 -Addtion (+)")
        print("2 -subtract (-)")
        print("3 -multiply(*)")
        print("4 -divide(/)")
        print("0 -exit")
        choice =input("Enter your choice:")
        if choice =="0":
            print("calculator closed.")
            break
        if choice not in ("1","2","3","4"):
            print("Invalid menu option!")
            continue
        try:
            a=float(input("enter a fist number: "))
            b=float(input("enter a second number: "))
        except ValueError:
                print("please enter vaild numbers!")
                continue
        if choice =="1":
            result=add(a,b)
            print("addition result: ",result)

        if choice =="2":
            result=sub(a,b)
            print("subtraction  result: ",result)


        if choice =="3":
            result=mult(a,b)
            print("multiply result: ",result)

        if choice =="4":
            result=div(a,b)
            print("divition result: ",result)

cal()