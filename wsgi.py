import os, sys, site
sys.path.insert(0, os.getenv('PROJECT_PATH'))
 
site.addsitedir(os.getenv('PYTHON_PATH') or '/usr/local/lib/python2.7/site-packages')
 
from app import create_app
 
app = create_app(os.getenv('FLASK_CONFIG'))
