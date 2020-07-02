import pandas as pd
import numpy as np
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def clean_dataset(df, width_criteria):
    assert isinstance(df, pd.DataFrame)
    df.dropna(inplace=True)
    df = df.drop(df[df.x >= width_criteria].index)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


pong = pd.read_csv("pong_game.csv")
pong.head()
pong.describe()
pong = pong.drop_duplicates()
pong.head()
pong.describe()
print(pong.head())
print(pong.describe())


#   Create file for ML
# sample = open ("pong_game.csv", "write")
# print("x, y, vx, vy, paddle.y", file = sample)


"""
X = pong.drop(columns = 'right_paddle.y')
y = pong['right_paddle.y']
#Run ML
from sklearn.neighbors import KNeighborsRegressor
clf = KNeighborsRegressor(n_neighbors = 3)
clf.fit(X, y)
df = pd.DataFrame(columns = ['x', 'y', 'vx', 'vy'])
    
    #toPredict = df.append({'x' : ball.x, 'y' : ball.y, 'vx' : ball.vx, 'vy' : ball.vy}, ignore_index = True)
    #MLposition = clf.predict(toPredict)

    right_paddle.update() #User controlled
    #right_paddle.update(MLposition) #ML controlled
    ball.update(right_paddle)

    print("{}, {}, {}, {}, {}" .format(ball.x, ball.y, ball.vx, ball.vy, right_paddle.y), file = sample) #prints data for ML
"""




