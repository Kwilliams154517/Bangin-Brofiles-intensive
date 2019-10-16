from flask import Flask, render_template
from pymongo import MongoClient 

client = MongoClient()
db = client.brofiles
brofiles = db.broifiles

app = Flask(__name__)

Brofiles =[
    { 'title': 'Brontent', 'description': 'Search' },
    { 'title': 'A new brofile', 'description': 'user created'}
]

@app.route('/')
def brofile_index():
    ''' Brofile Homepage '''
    return render_template('base.html', brofiles=brofiles.find())

@app.route('/home', methods=['GET', 'POST'])
def brofile_home():
    """ Brofiles creation page """
    return render_template('home.html')  

@app.route('/user/<brofile_id>')
def show_user_brofile(brofile_id):
    ''' Shows Brofile page'''
    # show_brofile()
    return render_template('show_brofile.html', brofile_id=brofile_id)



if __name__ == '__main__':
    app.run(debug=True)
