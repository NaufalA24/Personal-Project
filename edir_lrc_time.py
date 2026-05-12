import re
from pathlib import Path

def main() :
    
    lyricSource = input('input source file name including format　')
    lyricSource = Path(__file__).parent / f'{lyricSource}'
    finLyric = input('input finished file name including format　')
    addTime = float(input('input time difference, if lyric is delayed the difference is negative. format = [s][s].[ms][ms]'))

    # open source file
    with open(f'{lyricSource}' , encoding='utf-8') as script:

        # open target file
        with open(f'{finLyric}', mode='w', encoding='utf-8') as f :

            for line in script :

                # separate timestamp and lyric
                match = re.match(r'\[(.*?)\](.*)', line)

                timeStamp = match.group(1)
                lyric = match.group(2)

                # separate each time component
                timeComp = timeStamp.split(":")
                hour = int(timeComp[0])
                minute = int(timeComp[1])
                second = float(timeComp[2])

                second += addTime   # add time difference

                # check for overflow
                second, minute = overflowCheck(second, minute)
                minute, hour = overflowCheck(minute, hour)

                # format aligning
                minute = str(minute).zfill(2)
                hour = str(hour).zfill(2)
                second = f'{second:05.2f}'

                # rearrange and write to target file
                timeComp[0] = hour
                timeComp[1] = minute
                timeComp[2] = second
                timeStamp = f'{timeComp[0]}:{timeComp[1]}:{timeComp[2]}'
                f.write(f'[{timeStamp}]{lyric}\n')
            
def overflowCheck(x,y) :    # time overflow check function
    while x >= 60 :
        x -= 60
        y += 1
    return x, y


if __name__ == '__main__' :
    main()
