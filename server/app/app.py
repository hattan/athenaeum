from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation') #,doc=False

app.register_blueprint(blueprint)
app.config['SWAGGER_UI_JSONEDITOR'] = True

a_session = api.model('Session', 
    {
        'title' : fields.String('present this topic.'),
        'description' : fields.String('blah blah')
    }) #, 'id' : fields.Integer('ID')
 
sessions = []
session = {'name' : 'Intro to Python', 'id' : 1}
sessions.append(session)

@api.route('/sessions')
class Session(Resource):
    @api.marshal_with(a_session, envelope='data')
    def get(self):
        return sessions

    @api.expect(a_session)
    def post(self):
        print(api.payload)
        new_session = api.payload 
        new_session['id'] = len(sessions) + 1
        sessions.append(new_session)
        return {'result' : 'Language added'}, 201 

if __name__ == '__main__':
    app.run(debug=True)