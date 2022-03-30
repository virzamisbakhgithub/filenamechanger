import os

def main():
    i = 0
    #path going to the selected file folder u want to rename it
    path = "D:/APL Virza/assesmentpoint2/a/cekBulkRename/"
    for filename in os.listdir(path):
        content = "gambar " + str(i) + ".png"   #don't forget the extension
        source = path + filename
        content = path + content
        os.rename(source, content)
        i += 1

if __name__ == '__main__':
    main()