import math
import random

correct = 100
#random.randint(100, 999)

'''int型にしないと判定できない'''
input = int(input("３桁の文字列を入力してください: "))
print(input)
if input == correct:
    print("正解!")
else:
    print("不正解")