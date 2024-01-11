import os 
from uuid import uuid4

def rename_assignment_material(instance, filename):
    upload_to = 'assignment_materials'
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid4().hex[:10], ext)
    return os.path.join(upload_to,filename)


def rename_assignment_transaction(instance, filename):
    upload_to = 'assignment_transactions'
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid4().hex[:10], ext)
    return os.path.join(upload_to,filename)