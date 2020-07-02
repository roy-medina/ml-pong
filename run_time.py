import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv

# Obtain last index value of observation of ML data
def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 1
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [str(row_index), row[0], row[1]]
                data.append(columns)
    return data[-1][1]





'''
print(time.strftime("%H:%M:%S"))
print(datetime.datetime.now())


style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xs = []
    yx = []
    while

ani = animation.FuncAnimation(fig, animate, interval = float('inf'))
plt.show()
'''