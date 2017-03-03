from models import Blurb
from util import decode

def get_blurbs(id=""):
    blurbs = Blurb.m.find({"user": id}).all()
    blurbs = map(decode.decode_object_id, blurbs)
    return blurbs
