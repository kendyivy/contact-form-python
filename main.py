from flask import (Flask,
                    render_template,
                   request,
                   make_response,
                   redirect
                    )
import json
import models
from models  import Contact
 
app = Flask('app')
@app.route('/')
def index():
    models.initialize()
    return render_template("index.html")





@app.route('/contact', methods=['POST', 'GET'])
def register():
  data = dict(request.form.items())
  try:
      Contact.create(
            email=data.get('email', 'john@doe.com'),
            name=data.get('name', 'felician'),
            phone=data.get('phone', 10),
          )
      result = {
        'status': 'success',
        'message':'{} email unique'.format(user_data.get('email'))}
      return jsonify(result)
  except IntegrityError:
      result = {
      'status':'failed',
      'message':'{} email is not unique'.format(user_data.get('email'))}
  return jsonify(result)

    # if data.get('email', None):
    #     Contact.create(
    #         email=data.get('email', 'john@doe.com'),
    #         name=data.get('name', 'felician'),
    #         phone=data.get('phone', 10),
           
            
            
    #     )
    # return render_template("sign_up.html")


@app.route('/contacts')
def see_contacts():
    models.initialize()
    contacts = models.Contact.select()
    return render_template("contacts.html", contacts=contacts)
app.run(debug=True, host='0.0.0.0', port=8080)