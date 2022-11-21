import numpy as np
import pandas as pd
from betterplots import boxstripplot
import matplotlib.pyplot as plt 
import seaborn as sns  

np.random.seed(42)

# category = np.random.choice(['Plants', 'Animals'], 500)

# val = np.array(tuple(map(len,category))) + np.random.uniform(-2, 2, len(category))


# df = pd.DataFrame(dict(val=val, category=category, condition=np.digitize(val, np.linspace(val.min()*0.9,val.max()*1.1,5))-1))

# df = sns.load_dataset("tips")
df = sns.load_dataset("penguins")


plt.figure(num=1)
plt.ion()
plt.clf()

plt.subplot(1,3,1)

sns.boxplot(data=df, x='species', y='body_mass_g', hue='sex', width=.5)

sns.despine()

plt.subplot(1,3,2)
boxstripplot(data=df, x='species', y='body_mass_g', hue='sex', width=.3)
sns.despine()
plt.legend(loc=(1,.8), frameon=False)

# plt.subplot(1,3,3)
# ax = boxstripplot(data=df, x='category', y='val',
#                     width=.4, 
#                     hue='condition')
# sns.despine()
plt.show()