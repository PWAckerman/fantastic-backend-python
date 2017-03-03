from models import Project
from controllers import UserController
from util import decode


def save_project(request, id):
    data = request.json
    project = Project({"title": data["title"],
                        "platforms": data["platforms"],
                        "description": data["description"],
                        "screenshot": data["screenshot"],
                        "technologies": data["technologies"]})
    project.m.save()
    project = decode.decode_object_id(project)
    return UserController.add_project(id, project._id)
