def expmarks():    
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag
    from nltk.corpus import wordnet
    from userData import DataofUser
    import numpy as np
    import pandas as pd
    from rapidfuzz import process
    import Levenshtein

    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("wordnet")

    def nltk_to_wordnet(tag):
        if tag.startswith("J"):
            return wordnet.ADJ
        elif tag.startswith("V"):
            return wordnet.VERB
        elif tag.startswith("N"):
            return wordnet.NOUN
        elif tag.startswith("R"):
            return wordnet.ADV
        else :
            return None
    dictionary_job_level={"Entry_level":["Junior Data Engineer","Data Analyst","Buisness Intelligence(BI)",
                                     "Data Quality Analyst","Junior Data Scientist"],
                     "Mid_level":["Data Scientist","Data Engineer","Database Administrator(DBA)",
                                  "Data Architect","Buisness Intelligence (BI) Developer",
                                  "Machine Learning Engineer","Data Vizualization Specialist"],
                     "Senior_level":["Senior Data scientist","Senior Data Engineer","Lead Data Architect",
                                    "Data Consultant","Data Operation Specialist","Quantitative Analyst(quant)"],
                     "Executive_level":["Cheif Data Officer (CDO)","VP of Data","VP of Analytics","VP of Data Analysis",
                                        "Head of Data Science"]}
    data=pd.read_csv(r"Experience\experience.csv")
    df=DataofUser()
    experience_input=df["experience"]
    inputs=[]
    for i in experience_input:
        for j in i:
            inputs.append(j)
    n=len(inputs)
    exp=[]
    company=[]
    comapany_level=[]
    jobs=[]
    job_level=[]
    years=[]
    for i in inputs:
        sentence=i
        tokens=word_tokenize(sentence)
        tagged_tokens=pos_tag(tokens)
        noun=[word for word,tag in tagged_tokens if nltk_to_wordnet(tag)==wordnet.NOUN]
        adjective=[word for word,tag in tagged_tokens if nltk_to_wordnet(tag)==wordnet.ADJ]
        verb=[word for word,tag in tagged_tokens if nltk_to_wordnet(tag)==wordnet.VERB]
        adverb=[word for word,tag in tagged_tokens if nltk_to_wordnet(tag)==wordnet.ADV]
        numbers=[word for word in tokens if word.isdigit()]
        for i in range(len(numbers)):
            numbers[i]=int(numbers[i])
        print(noun)
        companyscore=[]
        comapnyname=[]
        for i in noun:
            if i=="Data" or i=="data":
                continue
            match=process.extractOne(i,data["Company"])
            companyscore.append(match[1])
            comapnyname.append(match[0])
        companyindex=companyscore.index(max(companyscore))
        companytext=comapnyname[companyindex]
        print(companytext)
        company.append(companytext)
        companyindex=companyscore.index(max(companyscore))
        comapany_level.append(data["company_level"][data[data["Company"]==companytext].index[0]])
        companyscore=[]
        comapnyname=[]
        for i in noun:
            if i=="Data" or i=="data":
                continue
            match=process.extractOne(i,data["jobs"])
            companyscore.append(match[1])
            comapnyname.append(match[0])
        companyindex=companyscore.index(max(companyscore))
        jobstext=comapnyname[companyindex]
        print(jobstext)
        jobs.append(jobstext)
        job_level.append(data["job level"][data[data["jobs"]==jobstext].index[0]])
        years.append(numbers[0])
        print(company)
        print(comapany_level)
        print(jobs)
        print(job_level)
        print(years)
    test=pd.DataFrame({"company":company,
                    "company_level":comapany_level,
                    "jobs level":job_level,
                    "jobs":jobs,
                    "years":years})
    import joblib
    from model_training import mapping
    company_m,company_l_m,jobs_level_m,job_m,decision_m=mapping()
    test["company"]=test["company"].map(company_m)
    test["company_level"]=test["company_level"].map(company_l_m)
    test["jobs"]=test["jobs"].map(jobs_level_m)
    test["jobs level"]=test["jobs level"].map(job_m)
    model=joblib.load("dtc.pkl")
    exp.append(model.predict(test.values))
    print(exp)
    print(exp[0])
    print(exp[0][0])
    expintext=[]
    for i in exp[0]:
        if i==2 or i==2.0:
            expintext.append("Good")
        elif i==1 or i==1.0:
            expintext.append("Excellent")
        elif i==0 or i==0.0 :
            expintext.append("Very Good")
    exp_level=[]
    for i in exp[0]:
        if i==2 or i==2.0:
            exp_level.append(1.0)
        elif i==1 or i==1.0:
            exp_level.append(3.0)
        elif i==0 or i==0.0 :
            exp_level.append(2.0)
    return company,jobs,expintext,exp_level