from flask import Flask, redirect, url_for, render_template, request,abort,flash
from werkzeug.utils import secure_filename
# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def index():
   return render_template('index.html')

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       if request.form['username'] == 'admin' :
#          return redirect(url_for('success'))
#       else:
#          abort(401)
#    else:
#       return redirect(url_for('index'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
   return render_template('login.html', error = error)


@app.route('/success')
def success():
   return 'logged in successfully'

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
	
if __name__ == '__main__':
   app.run(debug = True)