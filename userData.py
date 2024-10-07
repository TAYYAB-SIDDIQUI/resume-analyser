def DataofUser():
    import numpy as np
    import pandas as pd
    import ast
    df=pd.read_csv(r"data_of_user.csv")
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"],inplace=True)
    rough_data={}
    for i in df.columns:
        for j in range(len(df)):
            rough_data.update({i:df[i][j]})
    values=rough_data.values()
    keys=rough_data.keys()
    data_phase1=[]
    for i in values:
        if type(i)==str:
            if "[" and "]" in i:
                element=ast.literal_eval(i)
                data_phase1.append(element)
            else:
                data_phase1.append(i)
        else:
            data_phase1.append(i)
    print("data 1",data_phase1)
    rough=["\r<br>","\r\n","\n","\r","\t","<br>"]
    data_phase2=[]
    for i in data_phase1:
        if type(i)==str:
            for k in rough:
                if k in i:
                    i=i.replace(k,"resumebreaker101")
                    data_phase2.append([i])
        else:
            data_phase2.append([i])
        if [i] in data_phase2:
            continue
        else:
            data_phase2.append([i])
    final_data=[]
    for i in data_phase2:
        for j in i:
            if type(j)==str:
                j=j.split("resumebreaker101")
                final_data.append(j)
            else:
                final_data.append([j])
    print("final",final_data)
    processed_data={}
    for i in range(len(final_data)):
        processed_data.update({df.columns[i]:[final_data[i]]})
    final_df=pd.DataFrame(processed_data)
    print(final_df.to_string())
    return final_df