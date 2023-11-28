from flask import Flask, jsonify, request

from data.database import Database
from modules.helpers import UserSchema, RoleSchema, UserFeedbackSchema, UploadedDocSchema

database = Database()

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/user-feedback', methods=['GET', 'POST'])
def get_user_feedbacks():
    if request.method == 'POST':
        body = request.json
        feedback = body["user_id"]
        user_id = body["feedback"]
        return jsonify(UserFeedbackSchema().dump(database.create_user_feedback(user_id, feedback)))
    else:
        return jsonify(UserFeedbackSchema(many=True).dump(database.get_user_feedbacks()))
    
@app.route('/user-feedback/archive', methods=['PUT'])
def archive_user_feedback():
    print(request.args)
    user_feedback_id = request.args["user_feedback_id"]
    return jsonify(UserFeedbackSchema().dump(database.update_user_feedback(user_feedback_id, True)))

@app.route('/role', methods=['GET'])
def get_roles():
    return jsonify(RoleSchema(many=True).dump(database.get_roles()))

if __name__ == '__main__':
    app.run()