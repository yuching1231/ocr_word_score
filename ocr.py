from itertools import count
import cv2
import os
import pytesseract
import jieba
import json

def score(name_of_the_file, account_name, post_path):
    img_name = name_of_the_file + '.jpg'
    img_path = os.path.join(post_path, img_name)
    js_text_path = os.path.join(os.getcwd(), 'ocr_data', account_name, name_of_the_file + '.json')
    img = cv2.imread(img_path)
    seg_list = jieba.cut( pytesseract.image_to_string(img, lang = "chi_tra"), cut_all = False, HMM = True)
    text_score = 0
    jsfile = open(js_text_path, encoding='utf-8', mode='w')
    words = {}
    score = {}
    
    for word in seg_list:
        if word in positive_words:
            words[word] = 1
            print(word, " pos")
            text_score += 1
        elif word in negative_words:
            words[word] = -1
            print(word, " neg")
            text_score -= 1
        else:
            words[word] = 0

    score["score"] = text_score
    data = [words, score]
    json.dump(data, jsfile, ensure_ascii = False, indent=4)
    print('total: ', text_score)
    print()
    #cv2.imshow('Img', img)
    jsfile.close()
    return text_score

def account(account_path, account_name):  #processing every account in the dir "accounts"
    count_ind = 1
    pos_post = 0
    neg_post = 0
    zero_post = 0

    for filename in os.listdir(account_path):#process every post for the account
        path_of_the_post = os.path.join(account_path, filename)
        
        sc = score(filename, account_name, path_of_the_post)
        if sc > 0:
            pos_post += 1
        elif sc == 0:
            zero_post += 1
        else:
            neg_post += 1
        count_ind += 1

    
    js_result_path = os.path.join(os.getcwd(), 'ocr_data', account_name, 'result.json')
    result_file = open(js_result_path, encoding='utf-8', mode='w')
    attrib = {}
    attrib['Score > 0'] = pos_post
    attrib['Score = 0'] = zero_post
    attrib['Score < 0'] = neg_post
    json.dump(attrib, result_file, ensure_ascii = False, indent=4)
    result_file.close()

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