from flask import Flask, request, render_template, Response
import matplotlib.pyplot as plt
import csv, os
import numpy as np
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    height = weight = bmi = category = None
    if request.method == "POST":
        height = request.form.get("height", type=float)
        weight = request.form.get("weight", type=float)
        if height and weight and height > 0:
            bmi =  10000 * weight / (height * height) 
            save_bmi(height, weight, bmi)
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 24.9:
                category = "Normal"
            elif bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
    return render_template("index.html", height=height, weight=weight, bmi=bmi, category=category)

@app.route("/bmi_plot.png")
def bmi_plot():
    #load from csv
    bmi_values = load_bmi()
    if not bmi_values:
        bmi_values = [0]
    progr = list(range(1, len(bmi_values) + 1))
    
    fig, ax = plt.subplots()
    ax.plot(progr, bmi_values)
    ax.set_xlabel("Over Time")
    ax.set_ylabel("BMI")
    ax.set_title("BMI PROGRESSION XD")

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

CSV = "user/userdata.csv"

def save_bmi(height, weight, bmi):
    file_exists = os.path.exists(CSV)
    write_header = not file_exists or os.path.getsize(CSV) == 0

    with open(CSV, "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Height(cm)", "Weight(kg)", "BMI"])
        writer.writerow([height, weight, bmi])

def load_bmi():
    if not os.path.exists(CSV):
        return []
    with open(CSV) as file:
        reader = csv.DictReader(file)
        values = []
        for row in reader:
            try:
                values.append(float(row["BMI"]))
            except (ValueError, KeyError):
                continue
        return values


if __name__ == "__main__":
    app.run(debug=True)
