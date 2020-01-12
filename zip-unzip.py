import zipfile

zipfilePath = ("./CheXpert-v1.0-small.zip")
zip = zipfile.ZipFile(zipfilePath)
zip.extractall("./CheXpert-v1.0-small")
zip.close()
