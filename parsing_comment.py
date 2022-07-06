import encodings
from itertools import count
from collections import defaultdict
import pandas as pd
import cv2
import os
import csv
import pytesseract
import jieba

def score(name_of_the_file, account_name, post_path):

    comment_file = 'comment.csv'
    file_path = os.path.join(post_path, comment_file)

    df = pd.read_csv(file_path, encoding = 'utf-8', usecols = ['comment'])
    df = df.values.tolist()
    #print(df)
    seg_list = []
    for comm in df:
        for com in comm:
            seg_list += jieba.cut( str(com), cut_all = False, HMM = True)

    return seg_list

def account(account_path, account_name):  #processing every account in the dir "accounts"

    text_path = os.path.join(os.getcwd(), 'comment_data', account_name + 'comment_parsing.txt')
    text_file = open(text_path, 'w', encoding='utf-8')

    for filename in os.listdir(account_path):#process every post for the account
        path_of_the_post = os.path.join(account_path, filename)
        #score(filename, account_name, path_of_the_post)
        print(str(" ".join(score(filename, account_name, path_of_the_post))))
        print(str(" ".join(score(filename, account_name, path_of_the_post))), file = text_file)

    text_file.close()

jieba.case_sensitive = True
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

with open('dict_pos.txt', encoding='utf-8', mode='r') as f:
   positive_words = []
   for l in f:
       positive_words.append(l.strip())
 
with open('dict_neg.txt', encoding='utf-8', mode='r') as f:
   negative_words = []
   for l in f:
       negative_words.append(l.strip())

os.makedirs('comment_data', exist_ok = True)
path_of_every_account = os.path.join(os.getcwd(), "accounts") 
#in dir "accounts", contains all the ig accounts.
#for each account directory, every data of the post including image, likes etc
#is stored in a dir named in the form of "account_name + index"
for filename in os.listdir(path_of_every_account):
    path_of_the_account = os.path.join(path_of_every_account, filename)
    os.makedirs('./comment_data/' + filename , exist_ok = True)
    account(path_of_the_account, filename)