def solution(args):

    flg = 0
    str = ""
    for i in range(0,len(args)-2):
        if(args[i+1] == args[i]+1):
            if(flg == 0):
                if(args[i+2] == args[i]+2):
                    str += f'{args[i]}'
                    flg = 1
                else:
                    str += f'{args[i]}'
                    str += ","
        else:
            if(flg == 1):
                flg = 0
                str += '-'
                str += f'{args[i]}'
                str += ','
            else:
                str += f'{args[i]}'
                str += ','
    if(flg==1):
        if(args[i]+1 == args[i+1]):
            str += '-'
            str += f'{args[i+2]}'
        else:
            str += '-'
            str += f'{args[i+2]}'
            str += ','
            str += f'{args[i+2]}'
    else:
        str += f'{args[i+1]}'
        str += ','
        str += f'{args[i+2]}'

    print(str)
               
#arr = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
#It should work for random inputs too: '-52--50,-48,-46,-45,-42,-40--35' should equal '-52--50,-48,-46,-45,-42,-40--38,-35'


solution(arr)