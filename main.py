def is_weird_no():
    if 0<=n<=20:
        if(n%2!=0):
            print("Weird")
            return 0
        elif(2<=n<=5 and n%2==0):
            print("Not Weird")
            return 0
        elif(6<=n<=20 and n%2==0):
            print("Weird")
            return 0
    else:
            print("Not Weird")
            return 0
n = int(input())
print(is_weird_no())
