class Hint:
    input = 0
    def __init__(self, input, correct):
        self.input = input
        self.correct = correct
    
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
        list =[]
        for n in range(2,32):
            if self.correct % n == 0:
                list.append(n)
        print("求める数は", end="")
        for i in list:
            print(f"{i}  ", end="")
        print("の倍数です")
        #print(f"求める数は素数です")
        


            

