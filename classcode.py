
code_dic = {'국어':'962-429-6264', 
        '로봇요소':'239-723-0226',
        '사회':'399-616-3903',
        '미술':'708-980-3220',
        '진로':'이진욱- 863-494-3287/최대원- 475-845-2462',
        '회로이론':'915-066-4949',
        '영어':'853-740-7313',
        '체육':'797-371-4529',
        '전기기기':'230-168-5339',
        '기계요소설계':'류태열-275 604 2150(q95zHH)\n박정식-320-162-4722(2021)',
        '한국사':'895 188 4166'
        }


def class_code(class_name):
        global code_dic
        if class_name in code_dic.keys():
                #print(code_dic[class_name])
                return code_dic[class_name]
def code_if(code_msg):
        if code_msg in code_dic.keys():
                return 1
        else:
                return 0

def all_class_code():
        global code_dic
        temp = []
        temp.append('>>> ')
        for i,j in code_dic.items():
                temp.append(i+' '+j+'\n')
                #print(i+' : '+j)
        temp = ''.join(temp)
        return temp
                

#print(code_if('사회'))

#all_class_code()