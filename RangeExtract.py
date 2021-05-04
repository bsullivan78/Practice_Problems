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

    return str

solution(arr)
