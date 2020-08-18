import random
num=random.randint(1,10)
ans=int(input("請輸入數字:"))
if ans==1 and ans==2 and ans==3 and ans==4 and ans==5 and ans==6 and ans==7 and ans==8 and ans==9 and ans==10:
    ans=int(ans)
    if num==ans:
        print("恭喜答對")
    else:
        print("錯了U SUCK!!!")
else:
    print("不是數字")