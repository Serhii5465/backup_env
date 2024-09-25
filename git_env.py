import os
import posixpath
import datetime
import subprocess
import sys
from src import constants

DEST = posixpath.join(constants.ROOT_DIR_DEST_BACKUP, 'backup_git_cfg')
LOGS = posixpath.join(constants.LOGS_DIR, 'backup_git_cfg')
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
        "--log-file=" + LOG_FILE,
        '', 
        DEST
]

NAME_USER = os.getlogin()
ROOT_DIR_GIT_CFR = '/d/portable/git_home/'
list_git_files = [".ssh", 
                  ".bash_profile", 
                  ".bashrc", 
                  ".gitconfig", 
                  ".bash_history",
                  "scripts", 
                  ".bash_aliases", 
                  ".git_aliases",
                  ".ssh_aliases"
                ]

src = ''
out = None
for item in list_git_files:
    src = posixpath.join(ROOT_DIR_GIT_CFR, item)
    
    RSYNC_COMMAND[len(RSYNC_COMMAND) - 2] = src
    
    out = subprocess.run(RSYNC_COMMAND, stderr=sys.stderr, stdout=sys.stdout)

    if out.returncode != 0:
        sys.exit('Error\nCheck logs')