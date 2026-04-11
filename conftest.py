import os
import sys

# Ensure project root is in sys.path and cwd for config loading
project_root = os.path.dirname(__file__)
os.chdir(project_root)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
