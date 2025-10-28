from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    height = weight = bmi = category = None
    if request.method == "POST":
        height = request.form.get("height", type=float)
        weight = request.form.get("weight", type=float)
        if height and weight and height > 0:
            bmi =  10000 * weight / (height * height) 
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 24.9:
                category = "Normal"
            elif bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
    return render_template("index.html", height=height, weight=weight, bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
