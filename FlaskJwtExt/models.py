from FlaskJwtExt import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    """
    Users Model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    admin = db.Column(db.Boolean)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User ('{self.id}' ,'{self.public_id}', '{self.username}', '{self.password}', '{self.admin}' )"

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_publicid(cls, publicid):
        return cls.query.filter_by(publicid = publicid).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'public_id':x.public_id
               ,'username': x.username
               ,'password':x.password
               ,'admin':x.admin
            }
        return {'users':list(map(lambda x:to_json(x), cls.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Error on deletion'}

    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password, method='sha256')

    @staticmethod
    def verify_hash(password, hash):
        return check_password_hash(password,hash)


class Authors(db.Model):
    """
    Authors model
    """
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique = True, nullable=False)
    book = db.Column(db.String(20),unique = True, nullable=False)
    country = db.Column(db.String(50),nullable=False)
    booker_prize = db.Column(db.Boolean)
    user_id = db.Column(db.Integer , nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Author ('{self.id}' ,'{self.name}', '{self.book}', '{self.country}', '{self.booker_prize}', '{self.user_id}' )"

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'id':x.id
               ,'name': x.name
               ,'book':x.book
               ,'country':x.country
               ,'booker_prize': x.booker_prize
               ,'user_id':x.user_id
            }
        return {'authors':list(map(lambda x:to_json(x), cls.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Error on deletion'}

    @classmethod
    def delete_author(cls,authorid):
        try:
            num_rows_deleted = db.session.query(cls).filter_by(id = authorid).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Error on deletion'}


class RevokeTokenModel(db.Model):
    """
    Revoked Token Model
    """
    __tablename__ = 'Revoked_Tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls,jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)