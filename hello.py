from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html'), 200

@app.route('/continent/<string:name>')
def continent(name):
    #return name
	return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

