import uuid
from flask import request
from flask_restful import Resource, reqparse
from FlaskJwtExt.models import Users,Authors, RevokeTokenModel
from flask_jwt_extended import (create_access_token
                              , create_refresh_token
                              , jwt_required
                              , get_jwt_identity
                              , get_jwt
                              )

parser = reqparse.RequestParser()
parser.add_argument('username' , help = 'This field cannot be blank', required = True)
parser.add_argument('password' , help = 'This field cannot be blank', required = True)

#In case of successful registration or login we will return to user 2 tokens: access token and refresh token
#For tokens generation we use two functions: create_access_token and create_refresh_token
#Each function accepts at least one argument (identity (username)) but it can accept complex objects.
#Access token is needed to access protected routes.
#Refresh token is needed to reissue access token when it will expire.

class UserRegistration(Resource):
    """
    User Registration
    """
    def post(self):
        data = parser.parse_args()
        if Users.find_by_username(data['username']):
            return {'message':'User {} already exists'.format(data['username'])}

        new_user = Users (
            public_id=str(uuid.uuid4())
           ,username = data['username']
           ,password = Users.generate_hash(data['password'])
           ,admin=False
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity=data['username'])

            return {
                'message':'User {} was created'.format(data['username'])
               ,'access_token': access_token
               ,'refresh_token': refresh_token
            }
        except Exception as e:
            return {'message':'Error on user registration'}, 500

class UserLogin(Resource):
    """
    User Login
    """
    def post(self):
        data = parser.parse_args()
        current_user = Users.find_by_username(data['username'])
        if not current_user:
            return {'message':'User {} does not exist'.format(data['username'])}

        if Users.verify_hash(current_user.password,data['password']):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity=data['username'])

            return {'message':'Logged in as {}'.format(current_user.username)
                   ,'access_token':access_token
                   ,'refresh_token':refresh_token
                    }
        else:
            return {'message':'Wrong Credentials'}

class AllUsers(Resource):
    @jwt_required()
    def get(self):
        return Users.return_all()

    @jwt_required()
    def delete(self):
        return Users.delete_all()

class AuthorsAddAuthor(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user = Users.find_by_username(get_jwt_identity())

        new_author = Authors(
              name=data['name']
            , country=data['country']
            , book=data['book']
            , booker_prize=True
            , user_id=current_user.id
        )
        try:
            new_author.save_to_db()

            return {
                'message':'Author {} was created'.format(data['name'])
            }
        except Exception as e:
            return {'message':'Error on author creation'}, 500

class AllAuthors(Resource):
    @jwt_required()
    def get(self):
        return Authors.return_all()

    @jwt_required()
    def delete(self):
        data = request.get_json()
        if (data):
            authorid = data['authorid']
            return Authors.delete_author(authorid)
        else:
            return Authors.delete_all()

class UserLogoutAccess(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti'] #instead of get_raw_jwt
        try:
            revoked_token = RevokeTokenModel(jti=jti)
            revoked_token.add()
            return {'message':'Accesss token has been revoked'}
        except:
            return {'message':'Error occurred'},500

class UserLogoutRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        jti = get_jwt()['jti']
        try:
            revoked_token = RevokeTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message':'Error occurred'},500

class TokenRefresh(Resource):
    @jwt_required(refresh=True) #@jwt_refresh_token_required -> @jwt_required(refresh=True)
    #We mean by this decorator that we can access this route using only a refresh token not an access token
    def post(self):
        #To extract identity from the refresh token and then use this identity to create an access token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access-token':access_token}


class SecretResource(Resource):
    @jwt_required()
    def get(self):
        return {
            'answer':42
        }
