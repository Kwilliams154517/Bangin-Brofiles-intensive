from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient 
from bson.objectid import ObjectId

client = MongoClient()
db = client.brofiles
brofiles = db.brofiles

app = Flask(__name__)

# Brofiles =[
#     { 'title': 'Brontent', 'description': 'Search' },
#     { 'title': 'A new brofile', 'description': 'user created'}
# ]

@app.route('/')
def brofile_index():
    ''' Brofile Homepage '''
    return render_template('base.html')

@app.route('/home', methods=['GET', 'POST'])
def brofile_home():
    """ Brofiles creation page """
    return render_template('home.html', brofiles=brofiles.find())  

# @app.route('/user/<brofile_id>')
# def show_user_brofile(brofile_id):
#     ''' Shows Brofile page'''
#     # show_brofile()
#     return render_template('show_brofile.html', brofile_id=brofile_id)

@app.route('/brofiles/new')
def new_brofiles():
    """Create a new brofile."""
    return render_template('new_brofile.html')

@app.route('/brofiles', methods=['POST'])
def brofiles_submit():
    """Submit a new brofile."""
    brofile = {
        'name': request.form.get('name'),
        'bio': request.form.get('bio'),
        'bropiclink': request.form.get('bropiclink'),
    }
    brofile_id = brofiles.insert_one(brofile).inserted_id
    return redirect(url_for('brofiles_show', brofile_id=brofile_id))

@app.route('/brofiles/<brofile_id>')
def brofiles_show(brofile_id):
    brofile = brofiles.find_one({'_id': ObjectId(brofile_id)})
    return render_template('brofiles_show.html', brofile=brofile)

@app.route('/home/brofiles/edit/<brofile_id>')
def brofiles_edit(brofile_id):
    """ edits brofile profile """
    # brofiles = brofile.find_one({'_id': ObjectId(brofile_id)})
    # return redirect(url_for('brofiles_edit'))
    brofile = brofiles.find_one({'_id': ObjectId(brofile_id)})
    return render_template('brofiles_edit.html', brofile=brofile)

@app.route('/home/brofiles/delete/<brofile_id>', methods=['POST'])
def brofiles_delete(brofile_id):
    """ edits brofile profile """
    brofiles.delete_one({'_id': ObjectId(brofile_id)})
    return redirect(url_for('brofile_home'))

@app.route('/brofiles/<brofile_id>', methods=['POST'])
def brofiles_update(brofile_id):
    """Submit an edited brofile."""
    updated_brofile = {
        'name': request.form.get('name'),
        'bio': request.form.get('bio'),
        'bropiclink': request.form.get('bropiclink'),

    }
    brofiles.update_one({'_id': ObjectId(brofile_id)},{'$set': updated_brofile})
    return redirect(url_for('brofiles_show', brofile_id=brofile_id))

@app.route('/home/bang')
def show_bang_of_day():
    ''' shows bang of the day chart '''
    return render_template('botd.html')



if __name__ == '__main__':
    app.run(debug=True)
