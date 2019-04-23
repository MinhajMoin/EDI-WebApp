##from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
##    return "Hello to Our Web App"
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port = 5000)
    
