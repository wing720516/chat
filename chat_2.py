def read_file(filename):
    lines = []
    with open (filename, 'r',encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None #設空值，假設第一行沒有person，會有當掉的風險
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ') #切割完會形成清單，存入s
        time = s[0]
        person = s[1]
        if person == 'Allen':
            if s[2] == '貼圖': # 清單切割S[2:]第二的到最後 s[2:6]第二位置至第五位置 s[-2:]從後面第二個往前算到第一個
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else: 
                for m in s[2:]:
                    allen_word_count += len(m) #len算字數
        elif person == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else: 
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了', allen_word_count, '個字')
    print('Allen傳了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '張圖片')

    print('viki說了', viki_word_count, '個字')
    print('viki傳了', viki_sticker_count, '個貼圖')
    print('viki傳了', viki_image_count, '張圖片')


def write_file(filename, lines): # 檔名 & 存入的內容
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

        
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines) 
    
main()
