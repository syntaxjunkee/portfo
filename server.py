from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)



# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route('/')
def hello_world(username = None, post_id = None):
    return render_template('index.html', name=username, id= post_id )


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(f'{page_name}.html')


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])

def submit_form():

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou')
        except:
            return 'did not save to db'
    else:
        return "Something went wrong"