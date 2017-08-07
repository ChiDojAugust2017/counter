from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = '10b9443c4a16c0fd35afa2be12ae21d3'


@app.route('/', methods = ['GET','POST'])
def index():
        
    try:
        session['count'] += 1
        return render_template("index.html", number = session["count"])
    except:
        session['count'] =  0
        return render_template('index.html', number = session["count"])
    

@app.route('/show')
def show():
    session['count'] = 0
    return redirect ('/')


app.run(debug=True)