import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "animal": ["Cat", "dog", "DOG", "Rabbit", "rabbit", "Cat"],
    "weight_kg": [4.2, 12.0, 11.5, 2.1, 2.4, 300],
    "color": ["Black", "Brown", "brown", "white", "white", "Black"],
})

df["animal"] = df["animal"].str.strip().str.lower()
clean = df[df["weight_kg"] < 100].copy()

average = clean.groupby("animal")["weight_kg"].mean()

plt.bar(average.index, average.values)
plt.title("Average weight by animal")
plt.xlabel("Animal")
plt.ylabel("Weight (kg)")
#plt.show()
plt.plot(clean["weight_kg"], marker="o")
plt.title("Animal weights in the table")
plt.xlabel("Row number")
plt.ylabel("Weight (kg)")
plt.show()