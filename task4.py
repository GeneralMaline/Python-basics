import googletrans
translator = googletrans.Translator()
_file = open('text_4.txt', 'r', encoding='utf-8')
_file2 = open('text4_new.txt', 'w', encoding='utf-8')
stroki = _file.read()
for i in stroki.split("\n"):
    i = translator.translate(i, src='en', dest='ru').text
#    print(i, file=_file2)
    _file2.write(f'{i}\n')
_file.close()
_file2.close()