def Marks():
    from userData import DataofUser
    import numpy as np
    import pandas as pd
    import joblib
    from fuzzywuzzy import process
    df=DataofUser()
    countvector=joblib.load("CountVector.pkl")
    project_data=np.array(df["projects"])
    data=pd.read_csv(r"Data for project level\projects_level.csv")
    pr_texts=[]
    for i in project_data:
        for j in i:
            pr_texts.append(j.lower())
    vector=countvector.transform(pr_texts)
    from tensorflow.keras.models import load_model
    model=load_model("neunetforpr.h5")
    predicted=model.predict([vector])
    vals=[]
    for i in predicted:
        vals.append(np.argmax(i))
    classes=[]
    points=[]
    for i in vals:
        if i==0:
            classes.append("Advanced")
            points.append(3)
        elif i==1:
            classes.append("Beginner")
            points.append(1)
        elif i==2:
            classes.append("Expert")
            points.append(4)
        elif i==3:
            classes.append("Innovator")
            points.append(5)
        elif i==4:
            classes.append("Intermediate")
            points.append(2) 
    return pr_texts,classes,points       
        