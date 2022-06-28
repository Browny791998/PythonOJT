from flask import Flask,redirect, render_template,url_for,request,make_response

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


      
@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__=="__main__":
    app.run();