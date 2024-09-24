from flask import Flask,render_template,request,redirect,send_file
import os
from io import BytesIO
import matplotlib.pyplot as plt
import base64
app=Flask(__name__)
app.secret_key="supersecretkey"
app.config['UPLOAD_FOLDER']='static/uploads'
app.config['MAX_CONTENT_LENGTH']=16*1024*1024
ALLOWED_EXTENSION= {"jpg","png","jpeg","gif","jfif"}
def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSION
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Layout1")
def layouts1_selection():
    return render_template("Layout1.html")
@app.route("/Layout2")
def layouts2_selection():
    return render_template("Layout2.html")
@app.route("/Layout3")
def layouts3_selection():
    return render_template("Layout3.html")
@app.route("/Layout4")
def layouts4_selection():
    return render_template("Layout4.html")
def image_upload():
    if 'file' not in request.files:
        print(request.files)
        return redirect(request.url)
    file=request.files['file']
    if file.filename =='':
        print("2")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename=file.filename
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(file_path)
        return filename,file_path
@app.route("/data",methods=["GET","POST"])
def data():
    if request.method=="POST":
        phone=request.form.get("phone")
        try:
            number=int(phone)
            if len(str(number))!=10:
                phonemessage="please enter valid phone number"
            else :
                phonemessage=""
        except ValueError:
            phonemessage="Invalid Input, please enter numbers"
        email=request.form.get("email")
        if type(email[0])!=int or type(email[0])!=float:
            if email[0].isalpha():
                if email[-3]=="." or email[-4]==".":
                    if len(email)>5:
                        if "@" in email:
                            emailmessage=""
                        else:
                            emailmessage="Error in email : No @ in email"                           
                    else:
                        emailmessage="Error in email : len of mail is very low"
                else:
                    emailmessage="Error in email : '.' misplaced"
            else:
                emailmessage="Error in email : Start with alphabet"
        else:
            emailmessage="Error in email : Start with alphabet"       
        skill=request.form.get("skill")
        language=request.form.get("language")
        name=request.form.get("name")
        project=request.form.get("projects")
        experience=request.form.get("experience")
        education=request.form.get("education")
        link1=request.form.get("links")
        link=link1.split("\n")
        link_url=[]
        link_name=[]
        for i in link:
            element=i.split(",")
            link_url.append(element[0])
            link_name.append(element[1])
            print(link_url)
            print(link_name)
            url=[]
        for i in range(len(link_url)):
            html_texts=f'<a style="padding-right:4%;" href="https://{link_url[i]}" >{link_name[i]}</a>'
            url.append(html_texts)
        final="".join(url)
        import formal_text
        from nltk.tokenize import sent_tokenize
        formal_list=[]
        infos=[experience,project]
        sentences_list=[]
        for i in infos:
            for j in range(i.count("\n")):
                if i[i.find("\n")-1]!=".":
                    i=i.replace("\n"," . ")
            sentences_list.append(i)
        for i in sentences_list:
            formal_list.append(formal_text.main(i))
        print("formal",formal_list)
        phonehtml=phone.replace("\n","<br>")
        experiencehtml=formal_list[0].replace("$#","<br>")
        emailhtml=email.replace("\n","<br>")
        skillhtml=skill.replace("\n","<br>")
        languagehtml=language.replace("\n","<br>")
        namehtml=name.replace("\n","<br>")
        projecthtml=formal_list[1].replace("$#","<br>")
        educationhtml=education.replace("\n","<br>")
        global list_of_info
        global list_of_info_back
        list_of_info_back=[phone,email,skill,language,name,experience,project,education]
        from text_mistake import main
        textvalidation=[experience,project]
        textmessage=[]
        for i in textvalidation:
            textmessage.append(main(i))
        textmessage="\n".join(textmessage)
        print(textmessage)
        list_of_info=[phonehtml,emailhtml,skillhtml,languagehtml,namehtml,experiencehtml
                      ,projecthtml,educationhtml,final]
        global img
        global file_path
        img,file_path=image_upload()
    return render_template("preview.html",emailmessage=emailmessage,phonemessage=phonemessage,textmessage=textmessage)   
@app.route("/view")
def preview():
    if request.method=="GET":
        img_info=img
        list_of_data=list_of_info
        link_info=list_of_data[8]
        projects_info=list_of_data[6]
        experience_info=list_of_data[5]
        education_info=list_of_data[7]
        name_info=list_of_data[4]
        language_info=list_of_info[3]
        skill_info=list_of_info[2]
        email_info=list_of_info[1]
        phone_info=list_of_info[0]
        return render_template("final_resume.html",experience_info=experience_info,phone_info=phone_info,email_info=email_info,skill_info=skill_info,projects_info=projects_info,education_info=education_info,name_info=name_info,language_info=language_info,img_info=img_info,links=link_info)
    return render_template("index.html")
@app.route("/view1")
def preview1():
    if request.method=="GET":
        img_info=img
        list_of_data=list_of_info
        link_info=list_of_data[8]
        projects_info=list_of_data[6]
        experience_info=list_of_data[5]
        education_info=list_of_data[7]
        name_info=list_of_data[4]
        language_info=list_of_info[3]
        skill_info=list_of_info[2]
        email_info=list_of_info[1]
        phone_info=list_of_info[0]
        return render_template("final_resume2.html",experience_info=experience_info,phone_info=phone_info,email_info=email_info,skill_info=skill_info,projects_info=projects_info,education_info=education_info,name_info=name_info,language_info=language_info,img_info=img_info,links=link_info)
    return render_template("index.html")
@app.route("/df")
def show():
    if request.method=="GET":
        list_of_data=list_of_info_back
        projects_info=list_of_data[6]
        experience_info=list_of_data[5]
        education_info=list_of_data[7]
        name_info=list_of_data[4]
        language_info=list_of_info[3]
        skill_info=list_of_info[2]
        email_info=list_of_info[1]
        phone_info=list_of_info[0]
        projects_info=projects_info.replace("\n","")
        name_info=name_info.replace("\n","")
        phone_info=phone_info.replace("\n","")
        email_info=email_info.replace("\n","")
        skill_info=skill_info.replace("\n","")
        language_info=language_info.replace("\n","")
        experience_info=experience_info.replace("\n","")
        education_info=education_info.replace("\n","")
        import pandas as pd
        df=pd.DataFrame({
            "name":[name_info],"phone":[phone_info],"email":[email_info],
            "skills":[skill_info],"language":[language_info],"experience":[experience_info],
            "projects":[projects_info],"education":[education_info]
            })
        df.to_csv("data_of_user.csv",index=False)
        print("df",df)
        return "file created"
    return render_template("index.html")
@app.route("/report")
def marks():
    from plots import pltimg
    path,percentage_exp=pltimg()
    return render_template("marksheet.html",plot_img="static/plots/firsts.png",ovr_exp=percentage_exp)
if __name__=="__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)