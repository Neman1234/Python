import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
 
data = pd.DataFrame({
    "animal": ["cat", "dog", "rabbit", "cat", "dog"],
    "weight": [4.2, None, 2.1, 4.5, None],
    "colour": ["black", "brown", None, "white", "brown"]
})
 
msno.matrix(data)
plt.show()