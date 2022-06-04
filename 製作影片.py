# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 04:48:10 2022

@author: b4100
"""

import cv2
from os import listdir
from os.path import isfile, isdir, join

mypath = "./iimg"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)
F=files[0]
c=cv2.imread("./iimg/"+F)




'''
可調整幀數 fps
'''
fps=10  #29.97
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output4.mp4', fourcc, fps, (c.shape[1],c.shape[0]))   




# 指定要列出所有檔案的目錄


i=0

for f in files:

  fullpath = join(mypath, f)

  if isfile(fullpath):
    print("檔案：", f)
    img=cv2.imread("./iimg/"+f)
    out.write(img)


    if i%100==0:
        print(i)
    i+=1
    
    

    
out.release()
cv2.destroyAllWindows()  

