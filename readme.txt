"parsing_comment.py" 會將所有 "accounts" 資料夾裡的所有帳號的貼文的留言利用 jieba 斷詞，

"comment_grading.py" 則是將所有留言斷詞後計算分數。


=======================================================================================
資料夾路徑示意：

accounts 			-> hell_fun_www -> hell_fun_www1 -> comment.csv
parsing_comment.py	   hell_meme_ig    hell_fun_www2    hell_fun_www1.csv
comment_grading.py	   jc0615meme      hell_fun_www3    hell_fun_www1.jpg
comment_data       	 .              .                   hell_fun_wwwlikeuser1
	   			 .              .
	   			 .              .

=======================================================================================

comment_data 存放兩種資料：

directory： account_name + 'comment_parsing.txt' ： 所有留言斷詞後的結果

dircetory： account_name ：account_name + number.json 為斷詞後的分數總合
				 ：'result.json' 為此帳號的留言分數的分布