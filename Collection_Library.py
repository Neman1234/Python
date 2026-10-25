from collections import Counter

foods = ["Biyrani","Biyrani","Naan","Naan","Lasagna","Lasagna","Lasagna"]
counts = Counter(foods)

print(counts)
print(counts["Biyrani"])
print(counts.most_common(2))