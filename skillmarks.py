def skMarks():
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OrdinalEncoder
    from userData import DataofUser
    skills={"programming language":["python","r"],
            "statistical analysis":["statistics","probability theory"],
            "machine learning":["supervised machine learning","unsupervised machine learning","scikit-learn","Tensorflow","pytorch"],
            "data manipulation":["numpy","pandas"],
            "data vizualization":["data vizualization","matplotlib","seaborn","plotly","power bi","tableau"],
            "big data technoogy":["hadoop","spark","hive","kafka"],
            "sql/nosql":["sql","excel"],
            "cloud computing":["aws (amazon web service)","google cloud","microsoft azure"],
            "analytical skill":["problem solving","critical thinking","data wrangling","experiment design","model evaluation"],
            "mathematical skill":["linear algebra","optimizing technique"],
            "buisness and domain":["Buissness acumen","communication","storytelling with data"],
            "soft skills":["collaboration","adaptibility","curiosity","attention to detail"],
            "tool and techniques":["version control","etl (extract transform load)","apache","aiflow","Talend"],
            "Data ethics":["data maintenance","data privacy","data handling"]}
    skillsmarks={"programming language":[5,5],
            "statistical analysis":[5,5],
            "machine learning":[2,2,2,2,2],
            "data manipulation":[5,5],
            "data vizualization":[1.67,1.67,1.67,1.67,1.67,1.65],
            "big data technoogy":[2.5,2.5,2.5,2.5],
            "sql/nosql":[5,5],
            "cloud computing":[5,5],
            "analytical skill":[2,2,2,2,2],
            "mathematical skill":[5,5],
            "buisness and domain":[3.34,3.33,3.33],
            "soft skills":[2.5,2.5,2.5,2.5],
            "tool and techniques":[2,3,2,2,1],
            "Data ethics":[3.34,3.32,3.34]}
    skillslast=[]
    skillspoint=[]
    df=DataofUser()
    skillsofuser=df["skills"][0]
    print(skillsofuser)
    skillkey=skills.keys()
    skillvalue=skills.values()
    skillseries=pd.Series(skills)
    for i in skillseries.index:
        for j in skillsofuser:
            if j in skills[i]:
                skillslast.append(j)
                skillspoint.append(float(skillsmarks[i][skills[i].index(j)]))
    skillsnames=[]
    skillsnamestotal=[]
    for i in skillsmarks.keys():
        skillsnames.append(i)
        skillsnamestotal.append(float(sum(skillsmarks[i])))
    if sum(skillspoint)!=sum(skillsnamestotal):
        skillspoint.append(sum(skillsnamestotal)-sum(skillspoint))
        skillslast.append("unskilled")
    perskillpoints=[]
    for i in list(skillkey):
        oneskill=[]
        for j in skillsofuser:
            if j in skills[i]:
                oneskill.append(skillsmarks[i][list(skills[i]).index(j)])
            else:
                oneskill.append(0)
        perskillpoints.append(oneskill)
    pertotalskillpoints=[]
    for i in perskillpoints:
        pertotalskillpoints.append([sum(i)])
    for i in range(len(pertotalskillpoints)):
        pertotalskillpoints[i].append(10-sum(pertotalskillpoints[i]))
    print(skillsnames)
    print(skillslast)
    print(skillspoint)
    print(pertotalskillpoints)
    return skillsnames,skillslast,skillspoint,pertotalskillpoints