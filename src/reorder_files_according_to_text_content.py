import os
import shutil
from PIL import Image
import pytesseract
from PIL import Image
import pandas as pd
import datetime

input_dir = "./input"
output_dir = "./output"
text_content_file = "file_and_text.csv"

nb_items = 250
ORDER_COL_POS = 2
ORDER_COL_NAME = 'order'

def process_item(df_text_content,item):
        question = item + 1
        question_str =str(question)
        df_question = df_text_content[df_text_content['text'].str.contains('Q'+question_str+':')]
        df_answer = df_text_content[df_text_content['text'].str.contains('Q'+question_str+': Correct Answer')]
        df_question = df_question[df_question.isin(df_answer) == False].dropna()
        
        if (not df_question.empty) and (df_question.iat[0,ORDER_COL_POS]<0) :
            df_text_content.loc[df_question.index.tolist()[0], ORDER_COL_NAME] = question*10
            print("------------------------------")
            print("Question "+question_str+" : ")
            print(df_text_content.loc[df_question.index.tolist()[0], ORDER_COL_NAME])
       
        
        if (not df_answer.empty) and (df_answer.iat[0,ORDER_COL_POS]<0) :
            df_text_content.loc[df_answer.index.tolist()[0], ORDER_COL_NAME] = question*1000000 + question*100
            print("------------------------------")
            print("Answer "+question_str+" : ")
            print(df_text_content.loc[df_answer.index.tolist()[0], ORDER_COL_NAME])
 

def reorder_files():    
    print("Reorder files")
    df_text_content = pd.read_csv(input_dir+"/"+text_content_file,header=0) 
    df_text_content['order'] = -1
    for item in range(nb_items):
        process_item(df_text_content,item)

def main():
    # init output dirctory
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir)
    start_time = datetime.datetime.now()
    print(start_time)
    reorder_files();
    end_time = datetime.datetime.now()
    print("------------------------------")
    print("Started at : " + str(start_time))
    print("Ended   at : " + str(end_time))

if __name__ == '__main__':
    main()