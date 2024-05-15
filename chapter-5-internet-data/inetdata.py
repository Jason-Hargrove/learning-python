# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.jasonhargroveart.com/")
    print("result code:", weburl.getcode()) # 200 if ok, 400 if not found
    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()