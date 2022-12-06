from flask import Flask, render_template, request

# EB looks for an 'application' callable by default.
app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template('index.html')

#anak
@app.route('/form-anak')
def anak():
    return render_template('form-anak.html')

#dewasa
@app.route('/form-dewasa')
def dewasa():
    return render_template('form-dewasa.html')

#lansia
@app.route('/form-lansia')
def lansia():
    return render_template('form-lansia.html')

#imt
@app.route('/imt')
def imt():
    return render_template('imt.html')


if __name__ == "__main__":
    app.run(debug=True)