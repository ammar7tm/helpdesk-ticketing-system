from flask import Flask, render_template, request, redirect   # This import flask which handels everyhting with creating the app and connect to the server. render_tamplate runs the html file. 
import sqlite3


app = Flask(__name__)   # This is the app name 

# This is the function that runs when URL is clicked which Home Page 
@app.route("/")
def home():
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    cursor.execute("SELECT status, COUNT(*) FROM tickets GROUP BY status")
    counts = cursor.fetchall()
    connection.close()
    return render_template("home.html", counts=counts)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]

        connection = sqlite3.connect("tickets.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tickets (title, description, priority) VALUES (?, ?, ?)",
                       (title, description, priority))
        connection.commit()
        connection.close()

        return redirect("/")
    
    return render_template("submit.html")

@app.route("/tickets")
def tickets():
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tickets")
    all_tickets = cursor.fetchall()
    connection.close()
    return render_template("tickets.html", tickets=all_tickets)

@app.route("/update/<int:ticket_id>/<status>")
def update(ticket_id, status):
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
    connection.commit()
    connection.close()
    return redirect("/tickets")

if __name__ == "__main__":
    app.run(debug=True)  #start the server 