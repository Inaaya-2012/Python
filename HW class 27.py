
class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        
        words = self.input_string.split(" ")

        
        reversed_words = []

        index = len(words) - 1
        while index >= 0:
            if words[index] != "":
                reversed_words.append(words[index])
            index = index - 1

        
        reversed_string = " ".join(reversed_words)
        return reversed_string





reverser = StringReverser("Hello I am Inaaya")


result = reverser.reverse_words()


print("Reversed string:", result)

