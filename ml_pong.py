import pandas as pd

#Create file for ML
sample = open ("pong_game.csv", "write")
print("x, y, vx, vy, paddle.y", file = sample)

pong = pd.read_csv("pong_game.csv")
pong = pong.drop_duplicates()
pong.head()
pong.describe()

X = pong.drop(columns = "paddle.y")
y = pong['paddle.y']

#Run ML
from sklearn.neighbors import KNeighborsRegressor

clf = KNeightborsRegressor(n_neighbors = 3)

clf.fit(X, y)

df = pd.DataFrame(columns = ['x', 'y', 'vx', 'vy'])
    





