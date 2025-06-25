import math
import random
from hint import Hint 

def hint(input, correct, count):
    "ヒントが呼び出されるとインスタンス生成"
    instance1 = Hint(input, correct)
    if count == 1:
        instance1.range()

def check(A, B, count):
    if A == B:
        print("正解!")
    else:
        print("不正解")
        print(count)
        count+=1
        hint(input, correct, count)

count = 0
correct = 200
#random.randint(100, 999)

'''int型にしないと判定できない'''
input = int(input("３桁の文字列を入力してください: "))
print(input)
check(input, correct, count)
