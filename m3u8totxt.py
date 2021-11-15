
if __name__ == '__main__':
    filename = "基础电视直播源列表.txt"
    textfilename = "iptv-new.txt"
    names=[]
    links=[]
    name = "#NULL"
    fs = open(textfilename, 'w')
    with open(filename, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()  # 整行读取数据
            if not line:
                break

            if "#EXTINF:" in line:
                name=line.split(',')[1].strip()

            if "http://" in line:
                link=line.strip()
                fs.writelines("{},{}\n".format(name,link))
    fs.close()