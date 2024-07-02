from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_website():
    return render_template('website.html')

@app.route('/QandA')
def QandA():
    return render_template('QandA.html')

@app.route('/Works')
def Works():
    return render_template('Works.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/Info')
def Info():
    return render_template('Info.html')

@app.route('/Home')
def return_home():
    return render_template('website.html')

if __name__ == "__main__":
    app.run(debug=True)