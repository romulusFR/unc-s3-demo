"""Un module d'exemple"""

#%%

from pathlib import Path



def title(titre):
    """Affiche un titre"""
    print(titre.center(80, "-"))


title("un exemple")

p = Path(".")

print(p.absolute())
print("en cours")

#%%
def carre(x):
    """Calule le carré"""
    return x ** 2


l = [2 ** i for i in range(33)]
print(l)


def une_fonction():
    """Un test"""
    return 42

# %%

from numpy import random
import seaborn as sns

nombres = random.normal(10, 4, 20)

sns.histplot(nombres)

l = filter(lambda x : x >= 8 and x < 10, nombres)