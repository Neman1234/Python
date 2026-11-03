import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
sleep_data = pd.DataFrame({
    "pet": ["Cat", "Cat", "Cat", "Dog", "Dog", "Dog"],
    "hours_sleep": [14, 16, 15, 10, 12, 11]
})
 
sns.boxplot(data=sleep_data, x="pet", y="hours_sleep")
plt.title("Pet sleep hours")
plt.xlabel("Pet")
plt.ylabel("Hours of sleep")
#plt.show()
votes = pd.DataFrame({
    "game": ["Chess", "Tag", "Roblox", "Chess", "Tag",
             "Chess", "Roblox", "Tag", "Chess"]
})
 
sns.countplot(data=votes, x="game", hue="game", legend=False)
plt.title("Favourite games")
plt.xlabel("Game")
plt.ylabel("Number of votes")
plt.show()