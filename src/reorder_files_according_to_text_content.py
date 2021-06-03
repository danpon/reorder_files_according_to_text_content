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
    df_text_content = pd.read_csv(input_dir+"/"+text_content_file,header=0) 
    df_text_content['order'] = -1
    df_question = df_text_content[df_text_content['text'].str.contains('Q1:')]
    df_answer = df_text_content[df_text_content['text'].str.contains('Q1: Correct Answer')]
    df_question = df_question[df_question.isin(df_answer) == False]
    print("Question :")
    print(df_question.head(10))
    print("Answer :")
    print(df_answer.head(10))
 

def main():
    # init output dirctory
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir)
    reorder_files();

if __name__ == '__main__':
    main()