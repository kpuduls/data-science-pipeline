# Downloading data
import os
from definitions import comp_path
from kaggle.api.kaggle_api_extended import KaggleApi
import numpy as np
import sys
import zipfile


# Auth kaggle api
api = KaggleApi()
api.authenticate()

decision = input(" \n Do you want to search for a competition? (press y or n) ")

if decision == "y":
    while True:
        # Search the competition list
        search = input(" \n Please enter the search phrase: ")

        search_list = api.competitions_list(search = search)
        
        print(search_list)
        
        choose = input(" \n Enter index of the list to select the competition: (enter -1 to search for competitions again)")
        
        choose = int(choose)
        print(" \n You entered {0}".format(choose))
        print(" \n Competition {0} selected".format(search_list[choose]))
        print(type(str(search_list[choose])))
        if choose != -1:
            comp_name = str(search_list[choose])
            break

else:    
    print("\n Terminating the script \n")
    sys.exit()


# Create competition directory
# Define comp dir path
comp_dir = os.path.join(comp_path, comp_name)

isDir = os.path.isdir(comp_dir)

if isDir == True:
    print(" \n The competition directory already exists!!! Resolve the error!!! \n")
    print("Terminating the script")
    sys.exit()
else:
    # Create comp dir
    os.mkdir(comp_dir)
    print(" \n Competition '% s' directory created" % comp_name)

# Download comp data in the created comp dir
# Signature: competition_download_files(competition, path=None, force=False, quiet=True)
api.competition_download_files(comp_name, path = comp_dir)


with zipfile.ZipFile(os.path.join(comp_dir,comp_name + ".zip"), 'r') as zip_ref:
    zip_ref.extractall(comp_dir + "\data")
  
os.remove(os.path.join(comp_dir,comp_name + ".zip"))
