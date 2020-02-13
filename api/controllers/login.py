from flask import current_app as app
from flask import request
from flask_jwt_extended import create_access_token as create_jwt_token
from flask_restplus import Resource, fields, Namespace


api = Namespace('Login', description='authorize token to access services')

login_model = api.model('login', {
    'key': fields.String(required=True, description="provide key to get the token"),
})

"""
Login Api will create the JWT token after verifying the key sent by the client as parameter
:response : JWT TOKEN

"""
@api.route('/')
class Login(Resource):

    @api.expect(login_model)
    @api.response(403, 'Not Authorized')
    @api.response(500, 'Internal Server Error: Unable to fetch data for the submitted query')
    @api.response(200, 'success')
    def post(self):
        if not request.is_json:
            return {"message": "Missing JSON in request"}, 400

        key = request.json.get('key', None)
        if not key:
            return {"msg": "Missing key parameter"}, 400
        try:
            if key == app.config['JWT_SECRET_KEY']:
                access_token = create_jwt_token(identity=key, expires_delta=False)
                return {"jwt_token": access_token}, 200
            else:
                return {"message": "please enter valid key"}, 400
        except Exception as error:
            print("error---",error)


