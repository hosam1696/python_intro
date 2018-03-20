import os

# get files of directory
dir_path = os.path.join(os.getcwd(),'prank')
def secret_msg():
    imgs = filter(lambda img: os.path.splitext(img)[1] == '.jpg',os.listdir(dir_path))
    for img in imgs:
        os.rename(os.path.join(dir_path,img), os.path.join(dir_path,img.translate( '0123456789')))

secret_msg()