class Hint:
    input = 0
    def __init__(self, input, correct, count):
        self.input = input
        self.correct = correct
        self.count = count
    
    def range(self):
        i = 0
        print(self.input)
        for i in range(19):
            min = 100+i*50
            max = 150+i*50-1
            if min <= self.correct <= max:
                print(f"求める数は{min}から{max}の中です")
                break
        
    def multiple(self):
        n = 0
        for n in range(2,32):
            if self.correct % n == 0:
                print(f"求める数は{n}の倍数です")
                break
        print(f"求める数は素数です")
        


            

