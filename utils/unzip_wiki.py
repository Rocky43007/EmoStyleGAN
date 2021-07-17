from zipfile import ZipFile
#Used to unzip the zip file to where you choose.
def unZip(zipLoc, dirLoc):
# opening the zip file in READ mode
    with ZipFile(zipLoc, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
  
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(dirLoc)
        print('Done!')

unZip('datasets/wikiartimages.zip', 'datasets/wikiart')