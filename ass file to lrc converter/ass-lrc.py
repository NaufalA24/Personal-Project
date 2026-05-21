from pathlib import Path


def main() :
     while True :
        try :
            assSource = input('input source file name including format　')
            assSource = Path(__file__).parent / f'{assSource}'
            finLrc = input('input finished file name including format　')

            # open source file　ソースファイル開く
            with open(f'{assSource}' , encoding='utf-8') as script:
                Operate(finLrc, script)
                
            break
        
        except Exception as e :
            print(e)
            print('Error has occured, please try again')

            continue


def Operate(finLrc, script) :

    with open(f'{finLrc}', 'w', encoding='utf-8') as f:
        target_str = 'Dialogue:'
        for line in script:
            if target_str not in line :
                continue
            list_perline = [item.strip() for item in line.split(',', 9)]
            
            timeComp = (list_perline[1].split(':'))
            hour = int(timeComp[0])
            minute = int(timeComp[1])

            if hour != 0 :
                minute += hour * 60
                hour -= hour
            

            f.write(f"[{minute}:{timeComp[2]}]{list_perline[9]}\n")



if __name__ == '__main__' :
    main() 