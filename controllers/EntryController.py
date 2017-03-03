from models import Entry
from util import decode


def get_all_entries(id):
    entries = Entry.m.find({"user": id}).all()
    entries = map(decode.decode_object_id, entries)
    return entries


def save_entry(request, id):
    data = request.json
    entry = Entry({"user": id, "text": data["text"]})
    entry.m.save()
    entry = decode.decode_object_id(entry)
    return entry
