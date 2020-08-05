'''
1. 由使用者直接輸入欲掃描來源資料表之檔案的路徑
2. 程式將抓取T-SQL中位於FROM及JOIN後方的字串 (預設為資料表名稱)
3. 將字串清單寫入檔案 searchsrctables_output.txt 路徑為使用者輸入之路徑
4. 檔案內容格式 : 掃描檔案名稱,來源資料表名稱
'''

import os

file_path = input('請輸入欲掃描來源資料表之檔案的路徑:')                             # 使用者輸入檔案路徑
file_list = os.listdir(file_path)                                                   # 回傳路徑下的所有資料夾及檔案清單

table_list = []

for file in file_list:
    r_file_path_name = file_path + '\\' + file
    if os.path.isfile(r_file_path_name):
        f = open(r_file_path_name, 'r', encoding='utf-8', errors='ignore')
        word = f.read().replace('\n', ' ')                                        # 將換行符號移除
        word_list = [i for i in word.split(' ') if i != '']                        # 移除空元素
        for i in range(0, len(word_list)):
            if word_list[i].upper() == 'FROM' or word_list[i].upper() == 'JOIN':    # 抓取字串為FROM及JOIN的下一個元素
                if word_list[i+1].upper() not in ('(', '(SELECT', 'FOREIGN'):      # 排除'('、'SELECT'及'FOREIGN'
                    if (file + ',' + word_list[i+1]) not in table_list:             # 排除重複項目
                        table_list.append(file + ',' + word_list[i+1])              # 生成清單 (file name, source table name)
        f.close()


w_file_path_name = file_path + r'\searchsrctables_output.txt'                         # 產出檔案 searchsrctables_output.txt
f = open(w_file_path_name, 'w', encoding='utf-8')
for i in table_list:
    print(i.replace(')', ''))
    f.write(i.replace(')', ''))
    f.write('\n')
f.close()

print('請至您輸入的檔案路徑確認檔案 searchsrctables_output.txt 是否產出')
os.system('pause')