import shutil
import glob
import os

# copied = "20180314151206872_0001"
currentDir = './f1-2561'
copied = "B"

if __name__ == "__main__":
    getBaseDir = os.walk(currentDir).next()[1]
    for baseDir in getBaseDir:
        getSubDir = os.walk(currentDir + "/" + baseDir).next()[1]
        for subDir in getSubDir:
            files = glob.glob(currentDir + "/" + baseDir + "/" + subDir + "/*.jpg")
            for file in files:
               name = os.path.splitext(os.path.basename(file))[0]
               name = name + "B.jpg"
               shutil.copy2(currentDir + "/" + copied + ".jpg", currentDir + "/" + baseDir + "/" + subDir + "/" + name)

    # for folderIdx in [1, 2, 3, 4 ,5, 6, 7, 8, 9]:
    # for folderIdx in [5]:
        # for alpha in ['A', 'B']:
            # files = [ os.path.splitext(os.path.basename(x))[0] for x in glob.glob("./temp/" + str(folderIdx) + "/" + alpha + "/" + "*.jpg") ]
            # files = [x + "B" for x in files]
            # for myfiles in files:
                # shutil.copy2('./' + copied + ".jpg", "./temp/" + str(folderIdx) + "/" + alpha + "/" + myfiles + ".jpg")

