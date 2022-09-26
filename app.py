from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/helpful_links')
def helpful_links():
    return render_template('helpful_links.html')

@app.route('/essentials')
def essentials():
    return render_template('essentials.html')

@app.route('/admin-scripting')
def adminscripting():
    return render_template('admin-scripting.html')

@app.route('/networking-databases')
def networkingdatabases():
    return render_template('networking-databases.html')

@app.route('/IAM')
def IAM():
    return render_template('IAM.html')

@app.route('/endpoint-management')
def endpointmanagement():
    return render_template('endpoint-management.html')

if __name__ == '__main__':
    app.run(debug=True)
