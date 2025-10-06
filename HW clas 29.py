class RomanConverter:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number < 1 or number > 3999:
            raise ValueError("Roman numerals only support integers from 1 to 3999.")
        self.number = number

    def to_roman(self):
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = ""
        remaining = self.number

        for value, symbol in roman_numerals:
            while remaining >= value:
                result += symbol
                remaining -= value

        return result

    def __str__(self):
        return f"{self.number} -> {self.to_roman()}"



if __name__ == "__main__":
    converter = RomanConverter(2024)
    roman = converter.to_roman()
    print(f"Roman numeral for {converter.number} is: {roman}")

    # Optional: using __str__ method
    print(converter)

     