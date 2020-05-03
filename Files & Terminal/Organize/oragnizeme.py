import os
from pathlib import Path

SUBDIRS = {
    "DOCUMENTS": ['.pdf','.docx','.txt','.doc','.rtf','.pptx'],
    "AUDIO": ['.mp3','.m4a','.m4b'],
    "VIDEO": ['.mp4','.flv','.mkv','.divx','.mov','.avi'],
    "IMAGES": ['.jpeg','.png','.jpg','.svg'],
    "PHOTOSHOP":['.psd'],
    "CODE":['.java','.cpp','.kt']
}

def pickDict(value):
    for keys, suffixes in SUBDIRS.items():
        for suffix in suffixes:
            if suffix == value:
                return keys
    return "MISC"
def organize():
    for file in os.scandir():
        filePath =Path(file)
        suffix = filePath.suffix.lower()
        category = pickDict(suffix)
        categoryPath = Path(category)
        if categoryPath.exists()!=True:
            categoryPath.mkdir()
        filePath.rename(categoryPath.joinpath(filePath))
organize()