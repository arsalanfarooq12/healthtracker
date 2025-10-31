# Health Tracker BMI App

---

## Topic

A simple Flask-based web application that calculates Body Mass Index (BMI) and visualizes BMI changes over time.

---

## Goal

Currently, the app computes BMI from user inputs (height and weight) and stores each entry in a CSV file.
While “Health Tracker” is the name, the scope can expand beyond BMI to include more detailed health metrics.

---

## Other Ideas and Future Extensions

1. **User Authentication:**
   Add a login system to separate user data into individual CSV files.

2. **Categorization by Demographics:**
   Separate BMI categories and ranges for men, women, children, and others.

3. **Expanded Health Metrics:**
   Add tracking for blood pressure, sugar levels, and daily calorie intake.

4. **Your Ideas Here:**
   Open for additional suggestions.

---

## Working

As of now:

* The app is minimal and built on **Flask**.
* It calculates BMI and displays it along with a **BMI progression graph** using **Matplotlib (pyplot)**.
* Data persistence is handled with a single `.csv` file located at `user/userdata.csv`.
* The line graph updates each time a new entry is submitted.

This version is not multi-user safe; implementing separate storage per user would fix that.

---

## Requirements

* Python 3.x
* pip

Ensure both are installed before proceeding.

---

## Windows Setup

Run the script:

```bash
winsetup.bat
```

This will:

* Create a virtual environment
* Install dependencies
* Launch the Flask app

Access it in your browser at:

```
http://127.0.0.1:5000
```

---

## Linux Setup

Run the script:

```bash
. ./linuxsetup.sh
```

This automates virtual environment setup, dependency installation, and app startup.

---

## Notes

* Data is saved in `user/userdata.csv`.
* Each new entry updates the BMI trend line.
* Tested and stable on Linux.
* Windows script works under Wine; native testing still required.
