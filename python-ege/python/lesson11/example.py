rows = [(12, 80), (3, 95), (7, 80), (9, 95)]
ordered = sorted(rows, key=lambda row: (-row[1], row[0]))
for number, score in ordered:
    print(number, score)
