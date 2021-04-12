from FlaskJwtExt  import app, api, db, jwt
from FlaskJwtExt.models import RevokeTokenModel

from flask_jwt_extended import JWTManager

@app.before_first_request
def create_all():
    db.create_all()


from FlaskJwtExt import resources

#Defining resources /  API endpoints
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
api.add_resource(resources.AuthorsAddAuthor, '/addAuthor')
api.add_resource(resources.AllAuthors, '/authors')


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(*args):
    jti = args[1]['jti']
    isrevoked = RevokeTokenModel.is_jti_blacklisted(jti)
    return isrevoked

from FlaskJwtExt.views import *

if __name__ == "__main__":
    app.run(debug=True)