from flask import request, url_for
from flask.ext.api import FlaskAPI, status, exceptions
from controllers import UserController, BlurbController, SkillsController
from controllers import EntryController, ProjectController
from util import encoder
jsonEncoder = encoder.JSONEncoder()

app = FlaskAPI(__name__)


@app.route("/api/user/<string:id>/", methods=['GET'])
def get_user(id):
    res = UserController.get_user(id=id)
    if not res:
        raise exceptions.NotFound()
    return res


@app.route("/api/user/<string:id>/blurbs", methods=['GET'])
def get_blurbs(id):
    res = BlurbController.get_blurbs(id)
    if not res:
        raise exceptions.NotFound()
    return res


@app.route("/api/skills/", methods=['GET', 'POST'])
def skills():
    if request.method == 'GET':
        res = SkillsController.get_all_skills()
        if not res:
            raise exceptions.NotFound()
        return res
    elif request.method == 'POST':
        res = SkillsController.save_skill(request)
        if not res:
            raise exceptions.NotFound()
        return res


@app.route("/api/user/<string:id>/entries", methods=['GET', 'POST'])
def user_entries(id):
    if request.method == 'GET':
        res = EntryController.get_all_entries(id)
        if not res:
            raise exceptions.NotFound()
        return res
    elif request.method == 'POST':
        res = EntryController.save_skill(request, id)
        if not res:
            raise exceptions.NotFound()
        return res


@app.route("/api/user/<string:id>/project", methods=['POST'])
def project(id):
    res = ProjectController.save_project(request, id)
    if not res:
        raise exceptions.NotFound()
    return res

if __name__ == "__main__":
    app.run(debug=True)
