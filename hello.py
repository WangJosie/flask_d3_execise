import json
from flask import Flask, render_template, request, redirect,url_for
from flask import session
from collections import OrderedDict

app=Flask(__name__)

stop_word=["PREDICTED","PREDICTED:", "hypothetical"]
@app.route('/')
def index():
        return render_template('/inform.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request. method=='POST':
        vd=request.form['dom'] 
        print vd
        fn=vd+'_dump'
        f=open(fn)
        dict=json.load(f)
        return render_template('result.html', result=dict)
    else:
        return render_template ('error.html')


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method  =='POST':
        vd=request.form ['dom']
        clusterid=request.form['clusterid']
        print vd, clusterid
        fn=vd+'_dump'
        f=open(fn)
        dict=json.load(f)
        text_list=dict[clusterid]
        wordcount={}
        words=[]
        for i in text_list:
            words=i['name'].split()
            for w in words:
                w=w.encode('utf-8')
                w=w.replace("(", "")
                w=w.replace(")", "")
                w=w.replace('"','')
                w=w.replace(";", "")
                w=w.replace(":","")
                if w not in stop_word:
                  if w not in wordcount:
                      wordcount[w] =1
                  else:
                      wordcount[w] += 1
        
        with open("static/tmp.csv", "wb") as output:
            output.writelines("label,count"+"\n")
            for k, v in wordcount.items():
                line=str(k )+","+str(v)
                output.writelines(line+"\n") 
    
        return redirect(url_for("drawCloud"))

@app.route('/drawCloud')
def drawCloud():
    return render_template('drawCloud.html')


if __name__=="__main__":
    app.run(debug =True)

