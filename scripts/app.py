from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Deutsches Wörterbuch für die Monate
    months = {
        1: "Januar", 2: "Februar", 3: "März", 4: "April",
        5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
        9: "September", 10: "Oktober", 11: "November", 12: "Dezember"
    }
    
    # Heutiges Datum automatisch berechnen
    today = datetime.now()
    day = today.day
    month = months[today.month]
    year = today.year
    todays_date = f"{day}. {month} {year}"
    
    # Übergibt das Datum an die index.html im templates-Ordner
    return render_template("index.html", date=todays_date)

if __name__ == "__main__":
    app.run(debug=True)