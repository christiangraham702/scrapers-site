from application import app
from flask import render_template, request, Response, json


job_data = [{"jobID":"01", "website":"test.com", "query":"orange", "item_count":"5839", "date":"042021", "send_data":"email me"},
                {"jobID":"02", "website":"test.com", "query":"orange", "item_count":"5839", "date":"042021", "send_data":"email me"},
                {"jobID":"03", "website":"test.com", "query":"orange", "item_count":"5839", "date":"042021", "send_data":"email me"}]


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
@app.route('/jobs/<spider>') # <spider> is a variable, to pass to the template, here it is the name of the spider
def jobs(spider="all"): #defaults to showing all jobs
    return render_template('courses.html', job_data=job_data, spider=spider) #so we can use it in the template

@app.route('/send_data', methods=['POST', 'GET'])
def send_data():
    id = request.form.get('jobID')
    website = request.form.get('website')
    query = request.form.get('query')
    item_count = request.form.get('item_count')
    date = request.form.get('date')
    spider = request.form.get('spider')
    return render_template('send_data.html', send_data=True, data = {"jobID":id, "website":website, "query":query, "item_count":item_count, "date":date, "spider":spider})

@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
    if idx == None:
        json_data = job_data
    else:
        json_data = job_data[int(idx)]

    return Response(json.dumps(json_data), mimetype='application/json')