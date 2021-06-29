import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 

df = pd.read_csv('Data.csv')
weight_list = df['Weight(Pounds)'].to_list()

mean = statistics.mean(weight_list)
median = statistics.median(weight_list)
mode = statistics.mode(weight_list)
std_deviation = statistics.stdev(weight_list)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(std_deviation*2), mean+(std_deviation*2)
third_std_deviation_start, third_std_deviation_end = mean-(std_deviation*3), mean+(std_deviation*3)

list_of_data_within_1_std_deviation = [result for result in weight_list if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in weight_list if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in weight_list if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(weight_list)))

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("std_deviation of this data is {}".format(std_deviation))

fig = ff.create_distplot([weight_list],['Result'],show_hist = False )
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0,0.17],mode = 'lines', name = 'STANDARD DAVIATION 1'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0,0.17],mode = 'lines', name = 'STANDARD DAVIATION 1'))
fig.show() 