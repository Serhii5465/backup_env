import sys
import wmi
import subprocess
from src import constants

def conv_path_win_to_unix(windows_path: str) -> str:
    s = subprocess.run(['cygpath', '--unix', windows_path], capture_output=True, text=True)
    return s.stdout.strip('\n')

def get_mnt_point() -> dict[str, str]:
    uuids_src = [
        constants.DEST_UUID_DELL_INSPIRON_3576,
        constants.DEST_UUID_MSI_GF63
    ]
    
    try:
        c = wmi.WMI()
        
        for i in c.Win32_LogicalDisk():
            for j in uuids_src:
                if i.VolumeSerialNumber and i.VolumeSerialNumber.strip() == j:
                    return conv_path_win_to_unix(i.DeviceID)
        
        sys.exit("UUID not found")

    except Exception as e:
        sys.exit(f"An error occurred: {e}")