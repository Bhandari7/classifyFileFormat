# Set the path to your folder for actions

import os.path

CWD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unStructuredData") #Set the current path
print(f"Current working directory is : {CWD}")

my_folder = CWD

#Walking through the directory tree.
# for root, dirnames, files in os.walk(CWD):
#     print(root, dirnames, files)

# Define the classification rules
classification_rules = {
    'Images':   ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.svg', '.webp'],
    'Videos':   ['.mp4', '.MP4', '.MOV'],
    'Datasets': ['.csv', '.xlsx', '.json', '.sql'],
    'PDFs':     ['.pdf'],
    'Archives': ['.zip', '.rar'],
    'Other':    ['.AAE', '.WEBP', '.HEIC'] #other Iphone formats
}

# Automatic folder cleanup
DAYS_BEFORE_ARCHIVE = 30  # You can change this value based as per your requirement
ARCHIVE_ACTION = "move"  # "move" or "delete"
ARCHIVE_FOLDER = "Archived"
doArchive = True  #True--> to set archive action.

# ANSI escape code for green text
GREEN = '\033[32m'
RESET = '\033[0m'

# Log filename
log_filename = 'app.log'