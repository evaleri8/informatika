from itertools import product
for number, chars in enumerate(product("ABC", repeat=4), start=1):
    word = "".join(chars)
    if number % 2 == 0 and word[0] == "C" and word.count("A") == 1:
        print(number, word)
        break
