import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar.loc[0])
print(myvar.loc[1])
print(myvar.loc[2])
