from flask import Flask, render_template, request

# EB looks for an 'application' callable by default.
app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template('index.html')

#form
@app.route('/form')
def form():
    return render_template('form.html')

#imt
@app.route('/imt')
def imt():
    return render_template('imt.html')




if __name__ == "__main__":
    app.run(debug=True)