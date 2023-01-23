from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            nameOfStudent = body.get('nameOfStudent')
            if nameOfStudent is None or len(nameOfStudent) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            nameOfClass = body.get('nameOfClass')
            if nameOfClass is None or len(nameOfClass) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            nameOfHomework = body.get('nameOfHomework')
            nameOfHomework = body.get('nameOfHomework')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(nameOfStudent=nameOfStudent, 
                      nameOfClass=nameOfClass)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if nameOfHomework is not None:
                uo.nameOfHomework(nameOfHomework)
            # convert to date type

            _dateDue = body.get('_dateDue')
            if _dateDue is None or len(_dateDue) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            _dateDue = body.get('_dateDue')
    
            if _dateDue is not None:
                try:
                    uo._dateDue = datetime.strptime(_dateDue, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date of birth format error {_dateDue}, must be mm-dd-yyyy'}, 210
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {nameOfStudent}, either a format error or User ID {uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = User.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')