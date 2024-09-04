from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 15,00,000'},
        {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Teheran, Iran',
    'salary': 'RI. 18,00,000'},    
    {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'San Franisco, USA',
    'salary': '$. 120,000'},
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = "Jovian") # this is FLASK-specific

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)