import plotly.figure_factory as ff
import statistics
import random
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['temp'].tolist()

populaion__mean = statistics.mean(data)

std_deviation = statistics.stdev(data)

print('Population mean is:', populaion__mean)

print('Population Standard Deviation is:', std_deviation)

fig = ff.create_distplot([data], ['temp'], show_hist = False)

fig.show()

#dataset = []
#for i in range(0, 100):
#     random_index= random.randint(0,len(data))
#     value = data[random_index]
#     dataset.append(value)
# mean = statistics.mean(dataset)
# std_deviation = statistics.stdev(dataset)
#
# print("Mean of sample:- ",mean)
# print("std_deviation of sample:- ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

def std_deviation():
    mean_list = []

    for i in range(0, 1000):
         set_of_means= random_set_of_mean(100)
         mean_list.append(set_of_means)
    
    std_deviation = statistics.stdev(mean_list)

    print('Standard Deviation of sampling distribution :-', std_deviation)

std_deviation()