# Health Tracker BMI App

A simple Flask app that calculates your BMI and tracks progress over time.

---

## Requirements

1. Python 3.x
2. pip

> Ensure Python and pip are installed before proceeding.

---

## For Windows Users

Run the setup script:

```bash
winsetup.bat
```

This will:

* Create a virtual environment
* Install dependencies
* Launch the Flask app

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## For Linux Users

Run the setup script:

```bash
. ./linuxsetup.sh
```

This will handle environment setup, install dependencies, and start the Flask app.

---

## Notes

* User data is stored in `user/userdata.csv`.
* Each BMI entry updates the line chart automatically.
* Fully tested on Linux.
* Windows script tested via Wine; native testing recommended.
