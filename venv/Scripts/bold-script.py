#!"D:\Automation\WEB _×Ô¶¯»¯\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bold==0.3','console_scripts','bold'
__requires__ = 'bold==0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bold==0.3', 'console_scripts', 'bold')()
    )
