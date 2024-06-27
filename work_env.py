import os
import posixpath
import datetime
import subprocess
import sys
from src import constants

SRC = '/d/system'
DEST = posixpath.join(constants.ROOT_DIR_DEST_BACKUP, 'work_env')

LOGS = posixpath.join(constants.LOGS_DIR, 'backup_work_env')
TIMESTAMP = datetime.datetime.now().strftime('%d.%m.%Y_%H-%M-%S')
LOG_FILE = posixpath.join(LOGS, f"{TIMESTAMP}.log")

subprocess.run(['mkdir', '-p', DEST, LOGS], check=True, stderr=sys.stderr, stdout=sys.stdout)

RSYNC_COMMAND = [
        "rsync", 
        "--recursive", 
        "--perms", 
        "--times", 
        "--group", 
        "--owner",
        "--specials", 
        "--human-readable", 
        "--stats", 
        "--progress", 
        "--del",
        "--verbose", 
        "--out-format=%t %f %b", 
        "--exclude=__pycache__",
        '--exclude=PortableGit',
        "--log-file=" + LOG_FILE,
        SRC, 
        DEST
]

out = subprocess.run(RSYNC_COMMAND, stderr=sys.stderr, stdout=sys.stdout)

if out.returncode != 0:
    sys.exit('Error\nCheck logs')