##from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
##    return "Hello to Our Web App"
    a = render_template('index.html')
    return "<p>Hello</p>"
if __name__ == "__main__":
    app.run(threaded=True)
    
