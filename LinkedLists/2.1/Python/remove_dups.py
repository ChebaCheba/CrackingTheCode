import sys
import os
structure_path = os.path.split(os.path.split(sys.path[0])[0])[0]
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
import linked_list