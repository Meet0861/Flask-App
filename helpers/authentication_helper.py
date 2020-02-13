import jwt
from flask import current_app as app
from flask_jwt_extended import get_jwt_identity


class AuthenticationHelper:
    """
    Authentication Helper will verify the secret key after decoding it
    :result : return boolean to indicate the user is authorized or not
    """
    def verify_signature(self, args):
        auth_key = args['jwt-token']
        if auth_key:
            try:
                decoded_data = jwt.decode(str(auth_key), app.config['JWT_SECRET_KEY'])
            except jwt.DecodeError:
                app.logger.error({"message": 'Token is not valid'}, 401)
                return False
            if decoded_data is None:
                app.logger.error({"message": 'Token is not valid'})
                return False
            else:
                app.logger.info("signature verified")
                current_user = get_jwt_identity()
                app.logger.info({'logged_in_as': current_user})
                return True
        else:
            app.logger.error({"message": 'Auth token is not supplied'})
            return False
