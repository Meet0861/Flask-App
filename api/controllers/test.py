from flask_restplus import Resource, Namespace, fields
from helpers.authentication_helper import AuthenticationHelper
from flask_api import status
from flask import current_app as app

api = Namespace('Test', description='signature verification')

authentication_model = api.model('signature', {
    'name': fields.String(required=True, description="provide name to get the response"),
})
parser = api.parser()
parser.add_argument('jwt-token', type=str, help='contains jwt token in header', location='headers', required=True)

"""
Test ApI will show the actual use of JWT.
The user can only use the Api if the JWT token sent in the Authorization header is verified.
This is the Test API to show the application of JWT. one can directly embed any no of APIs in this application
:response : signature verification 

"""
@api.route('/')
class Test(Resource):

	@api.response(400, 'Bad Request')
	@api.response(500, 'Internal Server Error')
	@api.response(200, 'success')
	@api.expect(authentication_model)
	@api.doc(parser=parser)
	@api.doc(security='Authorize')
	def post(self):
		identity_status = AuthenticationHelper().verify_signature(parser.parse_args())
		if identity_status:
			data = api.payload
			app.logger.info(data)
			return '{message: Hi '+data['name']+'! you are successfullly logged in to the app. You are accessing the API now}', status.HTTP_200_OK
		else:
			return '{message: Incorrect token provided in input}', status.HTTP_401_UNAUTHORIZED

