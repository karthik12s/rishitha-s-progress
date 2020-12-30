from flask import Flask,redirect,url_for,render_template,request,flash
from pymongo import MongoClient
client=MongoClient('mongodb+srv://rishitha:rishitha@cluster0.tnlft.mongodb.net/result?retryWrites=true&w=majority')
db = client['result']
mains=db['main']
adv=db['advanced']
passwords={'skr':"karthik",'ris':'Rishitha','pcr':'Daddy','shb':'Mummy'}
app=Flask(__name__)
app.secret_key='abc'
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/main',methods=['GET','POST'])
def main():
    x=mains.find()
    i=0
    if request.method=='POST':
        for x1 in x:
            i=i+1
        a=request.form['d1']
        a=a.split('-')
        a=a[::-1]
        a1='-'.join(a)
        a=request.form['psd']
        if a in passwords:
            x=mains.insert_one({"Chemistry": request.form['c1'],"Date": a1,"Maths": request.form['m1'],"Physics": request.form['p1'],"Rank": request.form['r1'],"S NO": i+1,"TotalMarks": request.form['t1'],"Updated by":passwords[a]})
            flash("Record of Date "+a1+" Updated Successfully!!")
        else:
            flash("Enter valid Password")
        return(redirect(url_for('main')))
    else:
        date=[]
        rank=[]
        x=list(x)
        for i in x:
            date.append(str(i['Date']))
            rank.append(100-(int(i['Rank'])))
        return render_template('index.html',values1=rank,labels=date,d=x)
    return render_template('index.html')
@app.route('/adv',methods=['GET','POST'])
def adv1():
    x=adv.find()
    i=0
    if request.method=='POST':
        for x1 in x:
            i=i+1
        a=request.form['d1']
        a=a.split('-')
        a=a[::-1]
        a1='-'.join(a)
        a=request.form['psd']
        if a in passwords:
            x=adv.insert_one({"Chemistry": request.form['c1'],"Date": a1,"Maths": request.form['m1'],"Physics": request.form['p1'],"Rank": request.form['r1'],"S NO": i+1,"TotalMarks": request.form['t1'],"Updated by":passwords[a]})
            flash("Record of Date "+a1+" Updated Successfully!!")
        else:
            flash("Enter Valid Password")
        return(redirect(url_for('adv1')))
    else:
        date=[]
        rank=[]
        #print(list(x))
        x=list(x)
        for i in x:
            date.append(str(i['Date']))
            rank.append(100-(int(i['Rank'])))
        return render_template('adv.html',values1=rank,labels=date,d=x)
    return render_template('adv.html')
if __name__=='__main__':
    app.run(debug=True)
