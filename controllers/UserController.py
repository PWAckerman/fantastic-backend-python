from models import User
from models import Project
from models import Education
from models import Skill
from models import Learning
from bson.objectid import ObjectId


def get_user(id=""):
    user = User.m.find({"_id": ObjectId(id)}).first()
    user._id = str(user._id)
    user.projects = map(populate_with_model(Project), user.projects)
    user.education = map(populate_with_model(Education), user.education)
    user.skills = map(populate_with_model(Skill), user.skills)
    user.learnings = map(populate_with_model(Learning), user.learnings)
    return user


def add_project(id="", project_id=""):
    user = User.m.find_and_modify(query={"_id": ObjectId(id) },update={ "$push": { "projects": project_id }})
    user._id = str(user._id)
    return user


def populate_with_model(model):
    def return_function(id):
        res = model.m.find({"_id": ObjectId(id)}).first()
        res._id = str(res._id)
        return res
    return return_function
