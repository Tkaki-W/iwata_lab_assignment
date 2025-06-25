class Hint:
    input = 0
    def __init__(self, input, correct):
        self.input = input
        self.correct = correct
    
    def range(self):
        i = 0
        print(self.input)
        for i in range(19):
            print(i)
            min = 100+i*50
            max = 150+i*50-1
            if min <= self.correct <= max:
                print(f"求める数は{min}から{max}の中です")
        



            

