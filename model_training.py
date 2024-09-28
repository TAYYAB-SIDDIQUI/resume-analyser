def training():
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split,cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import OrdinalEncoder
    from imblearn.over_sampling import SMOTE
    from sklearn.metrics import mean_squared_error,classification_report,confusion_matrix
    df=pd.read_csv("Experience\experience.csv")
    df.dropna(inplace=True)
    print(df["experience"].value_counts())
    indexes=[i for i in range(len(df))]
    df=df.reindex(indexes)
    cols=[]
    for i in df.columns:
        cols.append(df[i])
    columns=df.columns
    oe=OrdinalEncoder()
    df[df.columns[0]]=oe.fit_transform(np.array(df[df.columns[0]]).reshape(-1,1))
    df[df.columns[1]]=oe.fit_transform(np.array(df[df.columns[1]]).reshape(-1,1))
    df[df.columns[2]]=oe.fit_transform(np.array(df[df.columns[2]]).reshape(-1,1))
    df[df.columns[3]]=oe.fit_transform(np.array(df[df.columns[3]]).reshape(-1,1))
    df[df.columns[4]]=oe.fit_transform(np.array(df[df.columns[4]]).reshape(-1,1))
    df[df.columns[5]]=oe.fit_transform(np.array(df[df.columns[5]]).reshape(-1,1))
    df[df.columns[6]]=oe.fit_transform(np.array(df[df.columns[6]]).reshape(-1,1))
    smore=SMOTE(random_state=42)
    x=df.drop(columns=["experience","Unnamed: 0"])
    print(x)
    y=df["experience"]
    x.dropna(inplace=True)
    y.dropna(inplace=True)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
    x_train,y_train=smore.fit_resample(x_train,y_train)
    from sklearn.naive_bayes import GaussianNB
    nb=GaussianNB()
    nb.fit(x_train,y_train)
    nbscore=nb.score(x_test,y_test)
    print(nbscore)
    lr=LogisticRegression()
    lr.fit(x_train,y_train)
    lrscore=lr.score(x_test,y_test)
    print(lrscore)
    print(np.sqrt(mean_squared_error(y_test,lr.predict(x_test))))
    lrcoef=lr.coef_
    lr_rmse=np.sqrt(mean_squared_error(y_test,lr.predict(x_test)))
    print(lr_rmse,lrscore)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    dtc=DecisionTreeClassifier()
    dtc.fit(x_train,y_train)
    dtc_score="%.1f" % dtc.score(x_test,y_test)
    dtc_rmse="%.1f" % np.sqrt(mean_squared_error(y_test,dtc.predict(x_test)))
    print(dtc_score,dtc_rmse)
    rfcl=RandomForestClassifier(n_estimators=100,random_state=42)
    rfcl.fit(x_train,y_train)
    rfcl_rmse= np.sqrt(mean_squared_error(y_test,rfcl.predict(x_test)))
    rfcl_score= rfcl.score(x_test,y_test)
    print(rfcl_score,rfcl_rmse)
    from sklearn.neighbors import KNeighborsClassifier
    k=3
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    knn_score=knn.score(x_test,y_test)
    knn_rmse="%.1f" % np.sqrt(mean_squared_error(y_test,knn.predict(x_test)))
    print(knn_score,knn_rmse)
    import joblib
    joblib.dump(dtc,"dtc.pkl")
    import matplotlib.pyplot as plt
    print(np.sqrt(mean_squared_error(y_test,dtc.predict(x_test))))
    import seaborn as sns
    sns.heatmap(confusion_matrix(y_test,dtc.predict(x_test)))
    plt.show()
    print((classification_report(y_test,dtc.predict(x_test))))
    cvs=cross_val_score(dtc,x,y,cv=5,scoring="neg_mean_squared_error")
    rmse=np.sqrt(-cvs)
    print(rmse)
    print(dtc.score(x_test,y_test))
    joblib.dump(oe,"dtcoe.pkl")
def mapping():
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OrdinalEncoder
    df=pd.read_csv("Experience\experience.csv")
    df.dropna(inplace=True)
    indexes=[i for i in range(len(df))]
    df=df.reindex(indexes)
    cols=[]
    for i in df.columns:
        cols.append(df[i])
    columns=df.columns
    oe=OrdinalEncoder()
    for i in columns:
        df[i]=oe.fit_transform(np.array(df[i]).reshape(-1,1))
    company_mapping={}
    company_level_mapping={}
    job_level_mapping={}
    jobs_mapping={}
    years_mapping={}
    experience_mapping={}
    for i in indexes:
        company_mapping.update({cols[1][i]:df[df.columns[1]][i]})
        company_level_mapping.update({cols[2][i]:df[df.columns[2]][i]})
        job_level_mapping.update({cols[3][i]:df[df.columns[3]][i]})
        jobs_mapping.update({cols[4][i]:df[df.columns[4]][i]})
        years_mapping.update({cols[5][i]:df[df.columns[5]][i]})
        experience_mapping.update({cols[6][i]:df[df.columns[6]][i]})
    return company_mapping,company_level_mapping,job_level_mapping,jobs_mapping,experience_mapping