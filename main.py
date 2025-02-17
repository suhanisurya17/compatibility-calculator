from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    love_score = sum(ord(char) for char in combined_names) % 100
    return love_score

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name1 = request.form.get("name1")
        name2 = request.form.get("name2")
        if name1 and name2:
            score = calculate_love_score(name1, name2)
            return render_template("index.html", name1=name1, name2=name2, score=score)
        else:
            return render_template("index.html", error="Please enter both names.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
