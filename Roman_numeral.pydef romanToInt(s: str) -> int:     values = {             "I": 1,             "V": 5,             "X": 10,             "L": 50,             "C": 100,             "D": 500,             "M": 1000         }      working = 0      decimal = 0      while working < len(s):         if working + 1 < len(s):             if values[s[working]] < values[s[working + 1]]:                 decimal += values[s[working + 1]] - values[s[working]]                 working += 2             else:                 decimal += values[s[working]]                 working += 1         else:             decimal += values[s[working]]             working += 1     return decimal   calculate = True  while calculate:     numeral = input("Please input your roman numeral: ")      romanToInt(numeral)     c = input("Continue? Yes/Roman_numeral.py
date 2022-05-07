def romanToInt(s: str) -> int:
    values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    working = 0

    decimal = 0

    while working < len(s):
        if working + 1 < len(s):
            if values[s[working]] < values[s[working + 1]]:
                decimal += values[s[working + 1]] - values[s[working]]
                working += 2
            else:
                decimal += values[s[working]]
                working += 1
        else:
            decimal += values[s[working]]
            working += 1
    return decimal


calculate = True

while calculate:
    numeral = input("Please input your roman numeral: ")

    romanToInt(numeral)
    c = input("Continue? Yes/No: ").lower
    if c == "no":
        calculate = False
