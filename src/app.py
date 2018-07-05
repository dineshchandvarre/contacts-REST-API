from flask import Flask,jsonify,request,abort
app = Flask(__name__)

contactList = [
    {
        'id': 1,
        'name': u'Dinesh',
        'phone': u'4696262056'
    },
    {
        'id': 2,
        'title': u'Sagar',
        'phone': u'9083434567'
    }
]

@app.route('/contact/<int:id>',methods= ['GET'])
def contacts(id):
    contacts=[contact for contact in contactList if contact['id']==id]
    if len(contacts)==0:
        abort(404)
    response=jsonify({'contact':contacts[0]})
    return response

@app.route('/contact/',methods= ['POST'])
def post_contacts():
    if not request.json and not 'name' in request.json:
        abort(404)
    contact={
	'id': contactList[-1]['id']+1,
        'name': request.json['name'],
        'phone': request.json['phone']
	}
    contactList.append(contact)
    return jsonify({'contact':contact})
# check for empty contacts and return 404 error

# post contact which adds a contact to the contactList

# update

# delete


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
