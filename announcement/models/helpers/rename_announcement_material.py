import os 
from uuid import uuid4

def rename_announcement_material(instance, filename):
    upload_to = 'announcement_materials'
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid4().hex[:10], ext)
    return os.path.join(upload_to,filename)