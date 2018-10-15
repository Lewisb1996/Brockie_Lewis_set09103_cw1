from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html'), 200

@app.route('/continent/<string:name>')
def continent(name):
    #return name
	return render_template(name+'.html')

@app.route('/Africa')
def africa():
    return render_template('africa.html')

@app.route('/Asia')
def asia():
    return render_template('asia.html')

@app.route('/America')
def america():
    return render_template('america.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

