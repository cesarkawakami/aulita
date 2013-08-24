import flask


app = flask.Flask(__name__)
app.config.from_object("aulita.config")


@app.route("/")
def hello():
    return flask.render_template("hello.html")


if __name__ == "__main__":
    app.run(app.config["HOST"], app.config["PORT"])
