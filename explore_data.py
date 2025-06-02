import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

#Load and prepare dataset
df = pd.read_csv("SMSSpamCollection",sep = "\t",header =None , names = ["label","message"])

#Display basic info 
print("First 5 rows:")
print(df.head())

print("\nClass Distribution:")
print(df['label'].value_counts())

#Optional: Visualize class distribution
sns.countplot(x='label',data=df)
plt.title("Spam vs Ham Count")
plt.show()

