import posixpath
from src import mnt

DEST_UUID_DELL_INSPIRON_3576 = '5837B806'

DEST_UUID_MSI_GF63 = '7E0E4F54'

ROOT_DEST = mnt.get_mnt_point()

ROOT_DIR_DEST_BACKUP = posixpath.join(ROOT_DEST, 'backups')

LOGS_DIR = posixpath.join(ROOT_DEST, 'logs')