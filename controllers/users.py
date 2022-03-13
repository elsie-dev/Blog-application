from flask_restx import Namespace, Resource, fields
from flask import request
from db import db

from models import User,Image


auth = Namespace('authenticated', description='Operations available to only authenticated')
public =Namespace('Public',description='Operations available to all users without authentication')



UserModel = auth.model('User', {
    'id': fields.Integer(readonly=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'user_name': fields.String(required=True),
    'password': fields.String(required=True),
    'account_created':fields.String(required=False),
    'account_updated':fields.String(required=False)
    
})

ImageModel = auth.model('Image',{
    'id': fields.Integer(readonly=True),
    'file_name': fields.String(required=True),
    'url': fields.String(required=True),
    'upload_date': fields.String(required=True),
    'user_id': fields.String(required=True)
})


UserModel = public.model('User', {
    'id': fields.Integer(readonly=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'user_name': fields.String(required=True),
    'password': fields.String(required=True),
    'account_created':fields.String(required=False),
    'account_updated':fields.String(required=False)
    
})

ImageModel = public.model('Image',{
    'id': fields.Integer(readonly=True),
    'file_name': fields.String(required=True),
    'url': fields.String(required=True),
    'upload_date': fields.String(required=True),
    'user_id': fields.String(required=True)
})



@auth.route('/v1/user/self')
class Index(Resource):
    @auth.doc('List_users')
    @auth.marshal_list_with(UserModel)
    def get(self):
        response = User.query.all()
        users = [res.to_json() for res in response]

        return users

    @auth.doc('update_user')
    @auth.marshal_with(UserModel)
    def put(self, id):
        req = request.get_json()
        user = User.query.filter_by(id=id).first()
        
        if 'first_name' in req:
            user.first_name = req['first_name']
        if 'last_name' in req:
            user.last_name = req['last_name']
        if 'user_name'  in req:
            user.user_name = req['user_name']
        if 'password'  in req:
            user.password = req['password']
        
        db.session.add(user)
        db.session.commit()

        return user

 


@auth.route('/v1/self/pic/')
@auth.param('id', 'User identifier')
@auth.response(404, 'User not found')
class Id(Resource):
    @auth.doc('Get_Image')
    @auth.marshal_with(ImageModel)
    def get(self):
        response = Image.query.filter_by(id=id).first()
        image = response.to_json()

        return image

    @auth.doc('Upload_Image')
    @auth.expect(ImageModel)
    def post(self):
        req = request.get_json()

        image= Image(file_name=req['file_name'],url=req['url'],user_id=req['user_id'])
        
        db.session.add(image)
        db.session.commit()

        return 'Image uploaded', 200
    
    



    @auth.doc('delete_image')
    def delete(self, id):
        image = Image.query.filter_by(id=id).first()

        db.session.delete(image)
        db.session.commit()

        return 'Image deleted', 200



# Images

@public.route('/v1/healthz/')
class Index(Resource):
  
    @public.doc('get_health')
    # @public.marshal_list_with(UserModel)
    def get(self):
        # response = User.query.all()
        # users = [res.to_json() for res in response]
        message = {"status":"server responds with 200 OK if it is healhty."}

        return message

    
@public.route('/v1/user')
class Index(Resource):

    @public.doc('Register_user')
    @public.expect(UserModel)
    def post(self):
        req = request.get_json()

        user = User(first_name=req['first_name'], last_name=req['last_name'],user_name=req['user_name'],password=req['password'])
        
        db.session.add(user)
        db.session.commit()

        return 'User registered', 200
