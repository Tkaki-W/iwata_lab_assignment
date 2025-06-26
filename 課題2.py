import math
import random
from hint import Hint 

    
def hint_output(answer, correct, count):
    "ヒントが呼び出されるとインスタンス生成"
    instance1 = Hint(answer, correct, count)
    if count == 1:
        instance1.range()
    elif count == 2:
        instance1.multiple()

def check(A, B):
    global count
    if A == B:
        print("正解!")
    else:
        print("不正解")
        count+=1
        print(count)
        hint_output(answer, correct, count)

count = 0
correct = random.randint(100, 999)
print(correct)

while True:
    print(count)
    '''int型にしないと判定できない'''
    answer = int(input("３桁の文字列を入力してください: "))
    print(answer)
    check(answer, correct)
