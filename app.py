from flask import Flask

app = Flask(__name__)
app.config["ENV"] = "production"
app.config["DEBUG"] = False

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

def create_app():
   return app


if __name__ == '__main__':
    app.run()
