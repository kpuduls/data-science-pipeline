# Downloading data
import os
import kaggle
import definitions.py

# Create competition directory

# Define comp dir path
comp_dir = os.path.join(comp_path, comp_name)
# Create comp dir
os.mkdir(comp_dir)
print("Competition '% s' directory created" % comp_name)


# Download comp data in the created comp dir
kaggle competitions download comp_name -p comp_dir
print("Competition data downloaded to '% s'" % comp_dir)