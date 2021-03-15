from pathlib import Path

def title(titre):
    print(titre.center(80,"-"))

title("un exemple")

p = Path(".")

# print(p.as_posix())
print("en cours")


def carre(x):
    return x**2
l = [2**i for i in range(33)]
print(l)
