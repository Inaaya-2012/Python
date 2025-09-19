class parrot:
    species = "Maccaw"
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = parrot("Kiwi",2)
p2 = parrot("Sky",3)
print(f"I am {p1.name} and my age is {p1.age} and I belong to the {p1.species} family") 
print(f"I am {p2.name} and my age is {p2.age} and I belong to the {p2.species} family")        