from models import Skill
from util import decode


def get_all_skills():
    skills = Skill.m.find().all()
    skills = map(decode.decode_object_id, skills)
    return skills


def save_skill(request):
    data = request.json
    skill = Skill({"name": data["name"], "icon": data["icon"], "type": data["type"]})
    skill.m.save()
    skill = decode.decode_object_id(skill)
    return skill
