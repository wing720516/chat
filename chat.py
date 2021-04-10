def read_file(filename):
    lines = []
    with open (filename, 'r',encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None #設空值，假設第一行沒有person，會有當掉的風險
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = "Tom" 
            continue
        if person: #如果person有值，則續run 
            new.append(person + ': ' + line)
    return (new)

def write_file(filename, lines): # 檔名 & 存入的內容
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
        
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines) 
    
main()
