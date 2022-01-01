import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

std_deviation=statistics.stdev(data)
population_mean = statistics.mean(data)

print("population_mean", population_mean)
print("std_deviation", std_deviation)

#code to find mean and std deviation of 100 data points

dataset=[]

for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
std_deviation2=statistics.stdev(dataset)
print("mean", mean)
print("std_deviation2", std_deviation2)

#function to get mean of given data samples.

def random_set_of_mean(counter):
    dataset1=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value1=data[random_index]
        dataset1.append(value1)
        
    mean=statistics.mean(dataset1)
    return mean
    
#function to plot mean on graph

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("sampling mean",mean)
    fig=ff.create_distplot([data], ["temp"], show_hist= False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1], mode="lines", name="mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
setup()