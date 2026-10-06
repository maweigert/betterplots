import matplotlib.pyplot as plt
import seaborn as sns
from betterplots import boxstripplot, set_style


set_style()

df = sns.load_dataset("penguins")


plt.figure(figsize=(5, 4))
boxstripplot(data=df, x="species", y="flipper_length_mm", hue="sex", width=0.3)
plt.title("Flipper Length", fontweight="bold")
plt.legend(loc=(1, 0.8))
plt.tight_layout()
plt.savefig("../images/example.png")
plt.show()
