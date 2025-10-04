class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + "(" + self.meaning + ")"

flash = []
while True:
    word = input("Enter the word : ")
    meaning = input("Enter the meaning : ")
    flash.append(flashcard(word,meaning))
    ch = input("Do you want to continue (y/n)")
    if ch.lower() == 'n':
        break;
print("The flashcards are")

for i in flash:
    print(">",i)
        
