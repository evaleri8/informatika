M, L, N = 70, 15, 1200
bits = (M - 1).bit_length()
bytes_per_record = (L * bits + 7) // 8
print(bits, bytes_per_record, bytes_per_record * N)
