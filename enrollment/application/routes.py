from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index=True)

@app.route('/scrape')
def scrape():
    return render_template('scrape.html', scrape=True)

@app.route('/data')
def get_data():
    return render_template('data.html', get_data=True)

@app.route('/stats')
def stats():
    return render_template('stats.html', stats=True)

@app.route('/login')
def login():
    return render_template('login.html', login=True)

@app.route('/jobs')
def jobs():
    job_data = [{"jobID":"01", "website":"test.com", "query":"orange", "items":"5839", "date":"042021", "send_data":"email me"},
                {"jobID":"02", "website":"test.com", "query":"orange", "items":"5839", "date":"042021", "send_data":"email me"},
                {"jobID":"03", "website":"test.com", "query":"orange", "items":"5839", "date":"042021", "send_data":"email me"}]
    print(job_data[0]['jobID'])
    return render_template('courses.html', job_data=job_data)

