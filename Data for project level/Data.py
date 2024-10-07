import pandas as pd
import numpy as np
txt_names=["beginner.txt","intermediate.txt","advance.txt","Expert.txt","Innovator.txt"]
text_list=[]
for i in txt_names: 
    with open(i,"r") as file:
        text=file.read()
        text_list.append(text)
list_of_texts=[]
for i in text_list:
    texts=[i]
    list_of_texts.append(texts)
for i in range(len(list_of_texts)):
    list_of_texts[i]=list_of_texts[i][0].split("\n")
list_of_df=[]
for i in list_of_texts:
    df=pd.DataFrame({"name":i})
    list_of_df.append(df)
df_beginner=list_of_df[0]
df_intermediate=list_of_df[1]
df_advance=list_of_df[2]
df_expert=list_of_df[3]
df_innovator=list_of_df[4]
df_beginner["Level"]=["beginner" for i in range(len(df_beginner))]
df_intermediate["Level"]=["intermediate" for i in range(len(df_intermediate))]
df_advance["Level"]=["advance" for i in range(len(df_advance))]
df_expert["Level"]=["expert" for i in range(len(df_expert))]
df_innovator["Level"]=["innovator" for i in range(len(df_innovator))]
final_data=pd.concat([df_beginner,df_intermediate,df_advance,df_expert,df_innovator])
final_data.to_csv("projects_level.csv")