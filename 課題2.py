import math
import random
from hint import Hint 

    
def hint_output(answer, correct):
    "ヒントが呼び出されるとインスタンス生成"
    instance1 = Hint(answer, correct)
    if count == 1:
        instance1.range()
    elif count == 2:
        instance1.multiple()
    else:
        print("もうヒントはないよ")

def check(A, B):
    global count
    if A == B:
        print("正解!")
    else:
        print("不正解")
        count+=1
        hint_output(answer, correct)

count = 0
correct = random.randint(100, 999)

while True:
    '''int型にしないと判定できない'''
    answer = int(input("３桁の文字列を入力してください: "))
    check(answer, correct)
