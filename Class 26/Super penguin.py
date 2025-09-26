class bird:
    def __init__(self):
        print("Bird is ready")
    
    def swim(self):
        print("Swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def run(self):
        print("I can run faster")

p1 = penguin()
p1.swim()
p1.run()                    