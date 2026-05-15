# This program will convert plain .txt lyric file to .lrc ready format
# It will also exclude the part tag usually used in Genius lyrics like "[Verse 1]"
# If you want to include tag you can disable this feature by deleting line 16 & 17

# This program DOES NOT time the lyrics automatically
# You have to input the time manually inside the blank [] bracket



list_perline = []

def main() :
    lyricSource = input('input file name excluding .txt　')
    with open(f'{lyricSource}.txt', encoding='utf-8') as lyric:
        for line in lyric :
            line = line.strip()
            if '[' and ']' in line :    # delete this if function if you want to include the lyric part tag
                continue
            list_perline.append(line)
    to_Lrc()
    
    
def to_Lrc() :
    finFile = input('input finished file name including file format　')
    with open(f'{finFile}', mode = 'w', encoding = 'utf8') as f :
        for line in list_perline :
            f.write(f'[]{line}\n')
        


if __name__ == '__main__' :
    main()