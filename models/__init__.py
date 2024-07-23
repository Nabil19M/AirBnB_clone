#!/usr/bin/python3
"""importing filestorage module
    """
from models.engine.file_storage import FileStorage
"""make an instance of filestorage to reload last saved objects
    """
storage = FileStorage()
storage.reload()
