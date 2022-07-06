from itertools import count
import cv2
import os
import pytesseract
import jieba

def score(name_of_the_file, account_name, post_path):
    img_name = name_of_the_file + '.jpg'
    img_path = os.path.join(post_path, img_name)
    img = cv2.imread(img_path)
    seg_list = jieba.cut( pytesseract.image_to_string(img, lang = "chi_tra"), cut_all = False, HMM = True)

    return seg_list

def account(account_path, account_name):  #processing every account in the dir "accounts"

    text_path = os.path.join(os.getcwd(), 'ocr_data', account_name, 'all_text_in_image.txt')
    text_file = open(text_path, 'w', encoding='utf-8')
    for filename in os.listdir(account_path):#process every post for the account
        path_of_the_post = os.path.join(account_path, filename)
        print(" ".join(score(filename, account_name, path_of_the_post)))
        print(" ".join(score(filename, account_name, path_of_the_post)), file = text_file)

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

os.makedirs('ocr_data', exist_ok = True)
path_of_every_account = os.path.join(os.getcwd(), "accounts") 
#in dir "accounts", contains all the ig accounts.
#for each account directory, every data of the post including image, likes etc
#is stored in a dir named in the form of "account_name + index"
for filename in os.listdir(path_of_every_account):
    path_of_the_account = os.path.join(path_of_every_account, filename)
    os.makedirs('./ocr_data/' + filename , exist_ok = True)
    account(path_of_the_account, filename)