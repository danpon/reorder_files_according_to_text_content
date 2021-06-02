import os
import shutil
from PIL import Image
import pytesseract
from PIL import Image
import pandas as pd

input_dir = "./input"
output_dir = "./output"
text_content_file = "file_and_text.csv"


def reorder_files():    
    print("Reorder files")

def main():
    # init output dirctory
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir)
    df_text_content = pd.read_csv(input_dir+"/"+text_content_file,header=1) 
    print(df_text_content.head(10))
    reorder_files();

if __name__ == '__main__':
    main()