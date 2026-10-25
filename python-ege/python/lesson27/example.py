events = [(0, 4), (1, 2), (2, 5), (4, 6), (5, 7), (7, 8)]
chosen = []
end = float("-inf")
for start, finish in sorted(events, key=lambda x: (x[1], x[0])):
    if start >= end:
        chosen.append((start, finish))
        end = finish
print(chosen)
