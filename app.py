from flask import Flask, request, render_template, Response, redirect, url_for, flash
import matplotlib
matplotlib.use("Agg")  # safe for headless servers
import matplotlib.pyplot as plt
import csv, os, io, datetime as dt
from typing import List, Optional

app = Flask(__name__)
app.config.update(
    SECRET_KEY="change-me",  # needed only if you use flash messages
    CSV_PATH=os.path.join(app.instance_path, "userdata.csv"),
)

# Ensure instance directory exists
os.makedirs(app.instance_path, exist_ok=True)


def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

CSV_PATH = "user/userdata.csv"

def save_bmi(height_cm: float, weight_kg: float, bmi: float) -> None:
    path = app.config["CSV_PATH"]
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["Timestamp", "Height(cm)", "Weight(kg)", "BMI"])
        writer.writerow([
            dt.datetime.now().isoformat(timespec="seconds"),
            f"{height_cm:.1f}",
            f"{weight_kg:.1f}",
            f"{bmi:.2f}",
        ])


def load_bmi() -> List[float]:
    path = app.config["CSV_PATH"]
    if not os.path.exists(path):
        return []
    values: List[float] = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                values.append(float(row["BMI"]))
            except Exception:
                continue
    return values


@app.route("/", methods=["GET", "POST"])
def index():
    height: Optional[float] = None
    weight: Optional[float] = None
    bmi: Optional[float] = None
    category: Optional[str] = None

    if request.method == "POST":
        try:
            height = float(request.form.get("height", "").strip())
            weight = float(request.form.get("weight", "").strip())
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive.")
            bmi = round(10000.0 * weight / (height * height), 2)
            category = classify_bmi(bmi)
            save_bmi(height, weight, bmi)
            # Post/Redirect/Get: prevent duplicate submissions on refresh
            return redirect(url_for("index", h=height, w=weight, b=bmi, c=category))
        except ValueError as ve:
            flash(str(ve), "error")
        except Exception:
            flash("Invalid input. Please enter numeric height and weight.", "error")
    else:
        # Support PRG result display
        if "b" in request.args:
            height = request.args.get("h", type=float)
            weight = request.args.get("w", type=float)
            bmi = request.args.get("b", type=float)
            category = request.args.get("c")

    return render_template("index.html", height=height, weight=weight, bmi=bmi, category=category)


@app.route("/bmi_plot.png")
def bmi_plot():
    values = load_bmi()

    if not values:
        fig, ax = plt.subplots(figsize=(5, 2.5))
        ax.axis("off")
        ax.text(0.5, 0.5, "No BMI data yet", ha="center", va="center", fontsize=12)
    else:
        x = list(range(1, len(values) + 1))
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(x, values, marker="o", color="#2563eb", linewidth=2)
        ax.set_xlabel("TIME-->")
        ax.set_ylabel("BMI")
        ax.set_title("HEALTH CHART")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=144)
    plt.close(fig)
    buf.seek(0)

    resp = Response(buf.getvalue(), mimetype="image/png")
    resp.headers["Cache-Control"] = "no-store"
    return resp


if __name__ == "__main__":
    app.run(debug=True)
