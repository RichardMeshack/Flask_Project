from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('Agro.html')


@app.route('/', methods=["POST", "GET"])
def massage():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("Agro.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>THANK YOU! </br>{usr} </h1>"


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

    

if __name__ == "__main__":
    app.run(debug=True)


