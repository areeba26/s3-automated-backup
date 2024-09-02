import shutil
import datetime
import os

def backup_file(source, destination):
    today = datetime.date.today()
    backup_fname= os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_fname,'gztar',source)

source = "Enter your source path"
destination = "Enter you destination path"

backup_file(source,destination)