import json
from flask import Flask, render_template, request, redirect,url_for
from flask import session


app=Flask(__name__)

stop_word=["PREDICTED", "hypothetical"]
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

@app.route('/word', methods=['GET', 'POST'])
def wordcloud():
    if request.method =='POST':
        vd=request.form['dom']
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
                if w not in stop_word:
                  if w not in wordcount:
                      wordcount[w] =1
                  else:
                      wordcount[w] += 1
        with open("tmp.json", "wb") as fp:
            json.dump(wordcount, fp)
    
        return render_template('word.html')


if __name__=="__main__":
    app.run(debug =True)

