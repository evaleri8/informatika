rules = {("q","0"):("1","R","q"), ("q","1"):("0","R","q"), ("q","_"):("_","S","q")}
tape = dict(enumerate("1010"))
pos, state = 0, "q"
steps = 0
while True:
    symbol = tape.get(pos,"_")
    new, move, state = rules[(state,symbol)]
    tape[pos] = new
    steps += 1
    if move == "S": break
    pos += 1 if move == "R" else -1
print("".join(tape.get(i,"_") for i in range(4)))
print(pos, steps)
