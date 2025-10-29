import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/egyptian-legal-extractor'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate your virtualenv
activate_this = os.path.expanduser('/home/yourusername/egyptian-legal-extractor/.venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Flask app
from app import app as application  # 'app' هو اسم متغير Flask في app.py