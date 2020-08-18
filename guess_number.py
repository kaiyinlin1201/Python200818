import random
num=random.randint(1,20)
i=1
print(num)
while i<6:
    ans=int(input("請輸入數字:"))
    if ans == num:
        print("恭喜答對",i,"次")
        break
    else:
        if ans>num:
            print("太大")
        else:
            print("太小")
    i=i+1   
        
        
