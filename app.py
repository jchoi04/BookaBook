from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# @app.out("/home")
#     def h

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'user_id' in session:
        return render_template('home.html', username=session['user_id'])
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = request.form.get('username')
        return redirect(url_for('home')) 
    return render_template('login.html')  

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session['user_id'] = request.form.get('username')
        return redirect(url_for('/'))  
    return render_template('signup.html') 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

    return render_template('contact.html')

@app.route("/search", methods=['GET'])
def search():
    search_query = request.args.get('q', '')
    return render_template('search_results.html', query=search_query)

@app.route("/math")
def Math():
    return render_template('math.html')

@app.route("/english")
def english():
    return render_template('english.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/forLang")
def forLang():
    return render_template('forLang.html')

@app.route("/arts")
def arts():
    return render_template('arts.html')

@app.route("/science")
def science():
    return render_template('science.html')

@app.route("/precalc")
def precalc():
    return render_template('precalc.html')

@app.route("/calc1")
def calc1():
    return render_template('calc1.html')

@app.route("/calc2")
def calc2():
    return render_template('calc2.html')

@app.route("/linAlg")
def linAlg():
    return render_template('linAlg.html')


if __name__ == '__main__':
    app.run(debug=True)
