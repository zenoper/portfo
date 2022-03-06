import email
import csv
from email import message
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:html_page>")
def html_page(html_page):
    return render_template(html_page)

def database_txt(data):
    with open('database.txt', 'a') as data_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = data_file.write(f'\n{email},{subject},{message}')

def database_csv(data):
    with open('database.csv', 'a', newline='') as data_file2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(data_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            database_txt(data)
            database_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database?! Try again'
    else:
        'Oooops, something went wrong. Try again!'