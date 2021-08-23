
if __name__ == '__main__':
    filename = "hangkang.m3u8"
    textfilename = "iptv-new.txt"
    names=[]
    links=[]
    fs = open(textfilename, 'w')
    with open(filename, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()  # 整行读取数据
            if not line:
                break

            if "#EXTINF:" in line:
                name=line.split(',')[1].strip()

            if "http" in line:
                link=line.strip()
                fs.writelines("{},{}\n".format(name,link))
    fs.close()