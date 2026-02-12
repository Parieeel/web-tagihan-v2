from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/laporan")
def laporan():
    return render_template("laporan.html")

@app.route("/pelanggan")
def pelanggan():
    return render_template("pelanggan.html")

@app.route("/tagihan")
def tagihan():
    return render_template("tagihan.html")

if __name__ == "__main__":
    app.run(debug=True)
