text = 'aabbbbccdeefccckkkd'

def coding(stroka):
    result = ''
    i = 1
    cnt = 1
    while i < len(stroka):
        if stroka[i] ==stroka[i-1]:
            cnt = cnt + 1
            i += 1
            if i == len(stroka):
                result += str(cnt) + stroka[i-1]
        else:
            if cnt == 1:
                result += stroka[i-1]
            else:
                result += str(cnt) + stroka[i-1]
            i += 1
            cnt = 1
            if i == len(stroka):
                if cnt > 1:
                    result += str(cnt) + stroka[i-1]
                else:
                    result += stroka[i-1]
   
    return result
print(coding(text))

def encoding(stroka):
    result = ''
    i = 0
    while i < len(stroka):
        if stroka[i].isdigit():
            result = result + int(stroka[i]) * stroka [i + 1]
            i = i+2
        else:
            result = result + stroka[i]
            i = i+1
    return result
    
text_1 = coding(text) 
print(encoding(text_1))