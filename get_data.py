import os
import zipfile

def unzip_file(filename):
    """unzip file to the working directory"""
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall('')
    zip_ref.close()

# download file:
# note see: https://github.com/Kaggle/kaggle-api
# for download instructions.
os.system('kaggle competitions download -c quora-question-pairs -w')

unzip_file('train.csv.zip')
unzip_file('test.csv.zip')
unzip_file('sample_submission.csv.zip')
