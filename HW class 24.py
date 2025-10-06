class Dog:
    
    species = "Canis familiaris"

    def __init__(self, name, breed):
        
        self.name = name
        self.breed = breed


dog1 = Dog("Bruno", "German Shepherd")
dog2 = Dog("Rocky", "Labrador")
dog3 = Dog("Luna", "Poodle")


print("Dog 1:")
print("Name:", dog1.name)
print("Breed:", dog1.breed)
print("Species:", Dog.species)
print()

print("Dog 2:")
print("Name:", dog2.name)
print("Breed:", dog2.breed)
print("Species:", Dog.species)
print()

print("Dog 3:")
print("Name:", dog3.name)
print("Breed:", dog3.breed)
print("Species:", Dog.species)
print()
