import plotly.express as px

from two_d8_class import Die

#create two D8
die_1 = Die()
die_2 = Die()

#Make some rolls and store results in a list.
results = []
for roll_num in range(1000): #rolling both dice 1000 time together
    result = die_1.roll_dice() + die_2.roll_dice()
    results.append(result)

#analyze the result
frequencies = []
max_result = die_1.num_side + die_2.num_side
poss_result = range(2, max_result+1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
title = " Results of Rolling Two D8 Dice 1,000 Times"
labels = {'x':'Sum of Two D8 Dice Numbers','y':'Frequency of The Sum'}
fig = px.bar(x=poss_result, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()