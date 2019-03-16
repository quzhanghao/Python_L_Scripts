def getMd5(path):
    dest=bytes.fromhex('00000030')
    with open(path,'rb') as fs:
        content = fs.read()
        md5Pos = 0
        while content:
            md5Pos = content.find(dest, md5Pos)
            if md5Pos==-1:
                break
            print(content[md5Pos+4:md5Pos+20].hex())            
            md5Pos += 20


if __name__=='__main__':
    getMd5(r'C:\Users\upython\Desktop\CRC16.vi')