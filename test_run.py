
import os
json_path = "C:\\Users\\lablocal\\Documents\\olfactory\\olfactometry\\test_config.json"
os.chdir("olfactometry")
print(os.getcwd())
import sys
print(sys.executable)
import olfactometry
olfactometry.main(json_path)