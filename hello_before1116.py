import json
from flask import Flask, render_template, request, redirect,url_for
from flask import session 

app=Flask(__name__)

@app.route('/')
def index():
        return render_template('/inform.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method=='POST':
        vd=request.form['dom'] 
        print vd
        fn=vd+'_dump'
        f=open(fn)
        dict=json.load(f)
        return render_template('result.html', result=dict)
    else:
        return render_template('error.html')



if __name__=="__main__":
    app.run(debug =True)

