import os
os.chdir('C:\\Users\\Sivak\\OneDrive\\Desktop\\Pantech_Courses\\Artificial_Intelligence\\Day12')
i=1
for file in os.listdir():
    src=file
    dst="2"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1