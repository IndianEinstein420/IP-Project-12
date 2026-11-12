import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def FilterAndPlot(req,TF = False):
    if choice == 1:
        Val_no = req_to_no1[req]
    if choice == 2:
        Val_no = req_to_no2[req]
        
    df_stat = pd.DataFrame(columns = [req])
        
    for i in list_players:
        df_stat.loc[i]=0
        
        if choice == 1:
            for j in batting.values:
                if i in j[0] and j[Val_no] != '-':
                    df_stat.loc[i,req] += int(j[Val_no])
        if choice == 2:
            for j in bowling.values:
                if i in j[0] and j[Val_no] != '-':
                    df_stat.loc[i,req] += int(j[Val_no])
                    
    df_stat1 = df_stat.sort_values(by=req,ascending = TF)
    df_stat1.head(10).plot(kind = 'bar')
    plt.show()    

def FilterAndPlotRatio(req,req2,req2_no,n,TF = False):
    Val = req_to_no_ratio[req]
    
    df_stat = pd.DataFrame(columns = Val)
        
    for i in list_players:
        df_stat.loc[i]=0
        if choice == 1:
            for j in batting.values:
                Valno1 = req_to_no1[Val[0]]
                Valno2 = req_to_no1[Val[1]]
                if i in j[0] and j[Valno1] != '-':
                    df_stat.loc[i,Val[0]] += int(j[Valno1])
                    df_stat.loc[i,Val[1]] += int(j[Valno2])
        if choice == 2:
            for j in bowling.values:
                Valno1 = req_to_no2[Val[0]]
                Valno2 = req_to_no2[Val[1]]
                if i in j[0] and j[Valno1] != '-':
                    df_stat.loc[i,Val[0]] += int(j[Valno1])
                    df_stat.loc[i,Val[1]] += int(j[Valno2])
                    
    for i in list_players:
        if df_stat.loc[i,req2] >= req2_no:
            df_stat.loc[i,req] = (df_stat.loc[i,Val[0]]/df_stat.loc[i,Val[1]]) * n
        
    df_stat1 = df_stat.sort_values(by=req,ascending = TF)
    df_stat1.head(10).plot(kind = 'bar', y= req)
    plt.show()
    
players = pd.read_csv("./PLAYERS_INFO.csv",usecols=['Team','Player'])
batting = pd.read_csv("./BATTING.csv",encoding="cp1252",usecols=['BATTING','RUNS','BALLS','MINUTES','FOURS','SIXES','STRICK RATE','MATCH'])
bowling = pd.read_csv("./BOWLING.csv",encoding="cp1252",usecols=['BOWLING','OVERS','MAIDEN','RUNS','WICKETS','FOURS','SIXES','ECONOMY','WIDE BALLS','NO BALLS','MATCH'])

req_to_no1 = {'Runs' : 1,'Sixes' : 5,'Fours' : 4,'Minutes' : 3,'Balls' : 2}
req_to_no2 = {'Wickets' : 4,'Maiden' : 2,'Runs' : 3,'Boundaries' : 11,'Balls' : 11}
req_to_no_ratio = {'Strike Rate' : ['Runs','Balls'],'Economy':['Runs','Balls']}
list_players = []
for i in players.values:
    list_players.append(i[1])

while True:
    print("STAT FINDER 101")
    print("1. Batting Records")
    print("2. Bowling Records")
    print("3. Show Match Data")
    print("4. Exit")
    choice = int(input('What Do You Want to do? '))

    if choice == 1:
        print("What Record?")
        print("1. Most Runs Scored")
        print("2. Highest Strike Rate (min. 20 balls)")
        print("3. Most Sixes")
        print("4. Most Fours")
        print("5. Most Minutes on Crease")
        print("6. Most No. of Balls Faced")
        choice2 = int(input('What Do You Want to See? '))

        if choice2 == 1:
            FilterAndPlot('Runs')

        if choice2 == 2:
            FilterAndPlotRatio('Strike Rate','Balls',20,100)

        if choice2 == 3:
            FilterAndPlot('Sixes')

        if choice2 == 4:
            FilterAndPlot('Fours')

        if choice2 == 5:
            FilterAndPlot('Minutes')

        if choice2 == 6:
            FilterAndPlot('Balls')

    if choice == 2:
        print("What Record?")
        print("1. Most Wickets Taken")
        print("2. Most Maidens Bowled")
        print("3. Least Runs Conceded")
        print("4. Most Boundaries Conceded")
        print("5. Best Economy (min. 4 overs bowled)")
        print("6. Most Balls Bowled")
        choice2 = int(input('What Do You Want to See? '))
        
        if choice2 == 1:
            FilterAndPlot('Wickets')

        if choice2 == 2:
            FilterAndPlot('Maiden')

        if choice2 == 3:
            FilterAndPlot('Runs',True)
            
        if choice2 == 4:
            bowling['BOUNDARIES'] = bowling['FOURS'] + bowling['SIXES']
            FilterAndPlot('Boundaries')

        if choice2 == 5:
            bowling["BALLS"] = (bowling['OVERS']//1) * 6 + (bowling['OVERS']%1) * 10
            FilterAndPlotRatio('Economy','Balls',24,6,True)

        if choice2 == 6:
            bowling["BALLS"] = (bowling['OVERS']//1) * 6 + (bowling['OVERS']%1) * 10
            FilterAndPlot('Balls')

    if choice == 3:
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
            
    if choice == 4:
        break
