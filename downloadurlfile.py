import urllib.request

url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=F4E1C662-BEBE-470D-8382-710DAF006840'

file_name = 'D:\\Python\\output\\查獲少年嫌疑犯人數.txt'
w_file = open(file_name, 'w', encoding='utf-8')

with urllib.request.urlopen(url) as f:
    content = f.read().decode('utf-8').rstrip()
    for l in content.split('\n'):
        print(l.replace('"', ''))
        w_file.write(l.replace('"', ''))

w_file.close()
