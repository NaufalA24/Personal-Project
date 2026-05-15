import re
from pathlib import Path

def main() :
    lyricSource = input('input source file name including format　')
    lyricSource = Path(__file__).parent / f'{lyricSource}'
    finLyric = input('input finished file name including format　')
    addTime = float(input('input time difference, if lyric is delayed the difference is negative. format = [s][s].[ms][ms]'))

    # open source file　ソースファイル開く
    with open(f'{lyricSource}' , encoding='utf-8') as script:
        Operate(finLyric, addTime, script)

def Operate(finLyric, addTime, script) :
    # open target file　ターゲットファイル作る
    with open(f'{finLyric}', mode='w', encoding='utf-8') as f :
        for line in script :
            if line=='\n' :
                continue
            
            # separate timestamp and lyric　タイムタグと歌詞分け
            match = re.match(r'\[(.*?)\](.*)', line)

            timeStamp = match.group(1)
            lyric = match.group(2)

            # separate each time component　タイムタグの中身分ける
            timeComp = timeStamp.split(":")
            timeFormat = len(timeComp)
            if timeFormat == 3 :
                hour = int(timeComp[timeFormat-3])
                minute = int(timeComp[timeFormat-2])
                second = float(timeComp[timeFormat-1])
            else :
                minute = int(timeComp[timeFormat-2])
                second = float(timeComp[timeFormat-1])


            second += addTime   # add time difference　時差を足す

            # check for overflow and format aligning　オーバーフローチェックとフォーマティング
            second, minute = overflowCheck(second, minute)
            if minute >= 60 or minute < 0 :
                minute, hour = overflowCheck(minute, hour)
            hour = str(hour).zfill(2)
            minute = str(minute).zfill(2)
            second = f'{second:05.2f}'
            timeComp[timeFormat-3] = hour
            timeComp[timeFormat-2] = minute
            timeComp[timeFormat-1] = second
            timeStamp = f'{timeComp[timeFormat-2]}:{timeComp[timeFormat-1]}'
            
            if hour != '00' :
                timeStamp = f'{timeComp[timeFormat-3]}:{timeComp[timeFormat-2]}:{timeComp[timeFormat-1]}'

            f.write(f'[{timeStamp}]{lyric}\n')
            
def overflowCheck(x,y) :    # time overflow check function
    if x>=0 :
        while x >= 60 :
            x -= 60
            y += 1
        
    else :
        while x<0 :
            x += 60
            y -= 1
            
    return x, y


if __name__ == '__main__' :
    main()
