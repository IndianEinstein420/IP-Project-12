import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def str_to_id(strr):
    lst = list(strr)
    n = 0
    for i in range(4,0,-1):
        n += int(lst[len(lst) - i])
        n = n * 10
    return (n/10 - 4657)

match_info = pd.read_csv('./Cricket_WC23.csv')
matches = pd.DataFrame(columns = match_info.columns)

T1 = input('Enter Team 1:')
T2 = input('Enter Team 2:')
t=1
for i in match_info.values:
    if (i[0] == T1 and i[1] == T2) or (i[1] == T1 and i[0] == T2):
        matches.loc[t] = i
        t += 1
        
if len(matches) == 1:
    match_id = str_to_id(matches.loc[1]['MATCH_ID'])
elif len(matches) == 2:
    s = 1
    for i in matches.values:
        print(s,i[0],'played',i[1],'at',i[4],'on',i[5])
        s += 1
    s_in = int(input('Which Match Do You Want? '))
    match_id = str_to_id(matches.loc[s_in]['MATCH_ID'])
else:
    print('Country Names Invalid')
    
match_prog1 = pd.read_csv('./BallbyBallData.csv',usecols = ['match_id','innings','ball','batting_team','runs_off_bat','extras','wicket_type'])
match_prog = match_prog1[match_prog1['match_id'] == int(match_id)]
inn1 = match_prog[match_prog['innings'] == 1]
inn2 = match_prog[match_prog['innings'] == 2]

list1 = [0]
list2 = [0]
out_list1 = []
out_list2 = []
ball = 1/6
for i in inn1.values:
    list1.append(ball)
    runs_off_ball = i[4] + i[5]
    list2.append(list2[-1] + runs_off_ball)
    if type(i[6]) != float:
        out_list1.append(ball)
        out_list2.append(list2[-1] + runs_off_ball)
    ball += 1/6

list3 = [0]
list4 = [0]
out_list3 = []
out_list4 = []
ball = 1/6
for i in inn2.values:
    list3.append(ball)
    runs_off_ball = i[4] + i[5]
    list4.append(list4[-1] + runs_off_ball)
    if type(i[6]) != float:
        out_list3.append(ball)
        out_list4.append(list4[-1] + runs_off_ball)
    ball += 1/6
    
plt.plot(list1,list2,label=inn1.iloc[0]['batting_team'])
plt.plot(list3,list4,label=inn2.iloc[0]['batting_team'])
plt.scatter(out_list1,out_list2)
plt.scatter(out_list3,out_list4)
plt.legend()
plt.show()





























    
    
