from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from data.database import Database
from modules.pdf_processor import pdf_processor
from modules.store_manager import store_manager
from modules.embedding_types import embedding_types
from modules.chat_chain import chat_chain
from data.database import Database
from modules.globals import pdf_files_dir
from modules.helpers import UserSchema, RoleSchema, UserFeedbackSchema, UploadedDocSchema, check_password

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

vector_store_manager = store_manager(embedding_type=embedding_types.OPENAIEMBEDDINGS)
    
database = Database()
database.init()

processor = pdf_processor(db=database, store=vector_store_manager)
processor.process(pdf_files_dir=pdf_files_dir)

chain = chat_chain(store=vector_store_manager)

@app.route('/user-feedback', methods=['GET', 'POST'])
def user_feedbacks():
    if request.method == 'POST':
        body = request.json
        user_id = body["user_id"]
        feedback = body["feedback"]
        return jsonify(UserFeedbackSchema().dump(database.create_user_feedback(user_id, feedback)))
    else:
        return jsonify(UserFeedbackSchema(many=True).dump(database.get_user_feedbacks()))
    
@app.route('/user-feedback/archive', methods=['GET', 'PUT'])
def archive_user_feedback():
    if request.method == 'PUT':
        user_feedback_id = request.args["user_feedback_id"]
        return jsonify(UserFeedbackSchema().dump(database.update_user_feedback(user_feedback_id, True)))
    else:
        return jsonify(UserFeedbackSchema(many=True).dump(database.get_user_feedbacks(only_archived=True)))

@app.route('/role', methods=['GET'])
def get_roles():
    return jsonify(RoleSchema(many=True).dump(database.get_roles()))

@app.route('/user', methods=['GET', 'PUT'])
def users():
    if request.method == 'PUT':
        body = request.json
        user_id = body["user_id"]
        role_id = body["role_id"]
        return jsonify(UserSchema().dump(database.update_user(user_id, role_id)))
    else:
        return jsonify(UserSchema(many=True).dump(database.get_users()))
    
@app.route('/user/custom-instructions', methods=['PUT'])
def update_custom_instructions():
    if request.method == 'PUT':
        body = request.json
        user_id = body["user_id"]
        custom_instruction = body["custom_instruction"]
        
        updated_user = jsonify(UserSchema().dump(database.update_custom_instruction(user_id, custom_instruction)))
        chain.reset_chat(custom_instructions=custom_instruction)
        return updated_user
    
    return jsonify("Error failed to update user custom instructions")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        body = request.json
        username = body["username"]
        password = body["password"]
        
        user = database.get_user(username)
        
        if check_password(password, user.password):
            user_data = UserSchema().dump(user)
            user_data["success"] = True
            return jsonify(user_data)
        
    return jsonify({ 
        "errorMessage": "Error failed to login",
        "success": False
    })
    
@app.route('/register', methods=['POST'])
def register():
    error = "Error failed to register"

    if request.method == 'POST':
        body = request.json
        username = body["username"]
        password = body["password"]
        
        user, error = database.create_user(username, password)
        
        if user:
            user_data = UserSchema().dump(user)
            user_data["success"] = True
            return jsonify(user_data)
        
    return jsonify({ 
        "errorMessage": error,
        "success": False
    })
    
@app.route('/document', methods=['GET', 'POST', 'DELETE'])
def document():
    if request.method == 'GET':
        return jsonify(UploadedDocSchema(many=True).dump(database.get_uploaded_docs()))
    elif request.method == 'POST':
        body = request.json
        username = body["username"]
        password = body["password"]
        
        user = database.create_user(username, password)
        
        if check_password(password, user.password):
            return jsonify(UserSchema().dump(user))
        
    return jsonify("Error failed to register")
    
@app.route('/chat', methods=['GET'])
def chat():
    if request.method == 'GET':
        user_id = request.args["user_id"]
        query = request.args["query"]
        
        return Response(chain.new_query_stream(query), mimetype='text/plain')
        
    return jsonify("Error failed to get chat response")

if __name__ == '__main__':
    app.run()