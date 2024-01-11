import os
from uuid import uuid4

def rename_subject_material(instance, filename):
    upload_to = 'subject_materials'
    ext = filename.split('.')[-1]  # Get the file extension
    # set filename as random string, limited to 10 characters
    filename = '{}.{}'.format(uuid4().hex[:10], ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def rename_class_record(instance, filename):
    upload_to = 'class_records'
    ext = filename.split('.')[-1]  # Get the file extension
    # set filename as random string, limited to 10 characters
    filename = '{}.{}'.format(uuid4().hex[:10], ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)