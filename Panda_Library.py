import pandas as pd

df = pd.DataFrame({
    "animal":["Cat","dog","DOG","Rabbit","rabbit","Cat"],
              "weight_kg":[4.2, 12.0, 11.5, 2.1, 2.4, 300],
              "color":["Black","Brown","brown","white","white",
                       "Black"]
                 })
print('Not clean data')
print(df)
df["animal"] = df["animal"].str.strip().str.lower()
print(df["animal"].tolist())
clean = df[df["weight_kg"] < 100].copy()
print(clean[["animal", "weight_kg"]])
print('Clean data')
print(clean)
print(clean.groupby("animal")["weight_kg"].mean().round(2))