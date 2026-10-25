energies = [1.0, 1.2, 1.7, 2.0, 2.4]
center = min(energies, key=lambda e: sum(abs(e - x) for x in energies))
median = sorted(energies)[len(energies) // 2]
print(center, median)
