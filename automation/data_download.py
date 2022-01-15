# Downloading data
import os
from definitions import comp_name, comp_path
from kaggle.api.kaggle_api_extended import KaggleApi

# Auth kaggle api
api = KaggleApi()
api.authenticate()

# Create competition directory
# Define comp dir path
comp_dir = os.path.join(comp_path, comp_name)

# Create comp dir
os.mkdir(comp_dir)
print("Competition '% s' directory created" % comp_name)


# Download comp data in the created comp dir
# Signature: competition_download_files(competition, path=None, force=False, quiet=True)
api.competition_download_files(comp_name, path = comp_dir)