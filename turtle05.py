import turtle
t=int(input("請輸入1到10中一個數字:"))
a=turtle.Turtle()
for i in range(t):
    a.forward(100)
    a.left(360/t)