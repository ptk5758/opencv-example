import pathlib
def getDocumentPath() -> str :
    return str(pathlib.Path.home().joinpath("Documents"))

def getPicturesPath() -> str :
    return str(pathlib.Path.home().joinpath("Pictures"))
# Pictures