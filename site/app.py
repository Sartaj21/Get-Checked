from flask import Flask, redirect, url_for, render_template, request, session, flash
import twitterStuff as ts
app = Flask(__name__)
formData = {}

@app.route("/")
def home():
   
    return render_template("index.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/quote",methods = ["POST","GET"])
def quote():
    if request.method == 'POST':
        quote = request.form['quote']
        author = request.form['author']
        date = request.form['date']
    
        value = ts.validate(author, quote, date)
        print(value)
        return render_template("quote.html", value = value)
    else:
        return render_template("quote.html")

@app.route("/fact")
def fact():
    return render_template("fact.html")



if __name__ == "__main__":
    app.run()

