import pandas as pd
import os


def transformation():
    if os.path.isfile("Input_FIle/APPL.csv"):
        data = pd.read_csv("Input_FIle/APPL.csv")
        moving_average = [None]

        for i in range(1,(data.shape[0]-1)):
            res=sum(data.iloc[[(i-1),i,i+1],1])/3
            moving_average.append(res)
        #compute the Simple Moving Average


        moving_average.append(None)
        new_moving_average = pd.DataFrame({'SMA_3' : moving_average})
        new_moving_average.index = data.index
        data = pd.concat([data,new_moving_average],axis=1)
        data.to_csv("Input_File/APPL.csv")

    else:
        print("The import file cannot be detected")





