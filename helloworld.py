
#!/usr/bin/python
from flask import Flask

PORT = 9090
MESSAGE = "In the Name of Allah, the Most Beneficent, the Most Merciful.!\n"
app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=PORT)
