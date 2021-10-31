import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean1 = st.mean(data)
stdev1 = st.stdev(data)
""" print(mean1)
print(stdev1)
 """
""" fig = ff.create_distplot([data], ["Math scores"], show_hist = False)
fig.show() """


def random_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_means = random_means(100)
    mean_list.append(set_of_means)

mean = st.mean(mean_list)
stdev = st.stdev(mean_list)
print(mean)
print(stdev)

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)

#Plotting the ranges of standard deviations
""" fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "stdev 1 start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "stdev 2 start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.17], mode = "lines", name = "stdev 3 start"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 3 end"))
fig.show()
 """

#Finding the mean of the 1st group & plotting
df = pd.read_csv('data1.csv')
data = df['Math_score'].tolist()
mean_sample1 = st.mean(data)
print(mean_sample1)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_sample1, mean_sample1], y = [0, 0.17], mode = "lines", name = "MEAN of sample 1"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 1 end"))
#fig.show() 

#Finding the mean of the 2nd group & plotting
df = pd.read_csv('data2.csv')
data = df['Math_score'].tolist()
mean_sample2 = st.mean(data)
print(mean_sample2)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_sample2, mean_sample2], y = [0, 0.17], mode = "lines", name = "MEAN of sample"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 2 end"))
#fig.show()


#Finding the mean of the 3rd group & plotting
df = pd.read_csv('data3.csv')
data = df['Math_score'].tolist()
mean_sample3 = st.mean(data)
print(mean_sample3)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_sample3, mean_sample3], y = [0, 0.17], mode = "lines", name = "MEAN of sample"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "stdev 3 end"))
#fig.show()

#Finding z-score
zScore = (mean_sample1 - mean)/stdev
print(zScore)