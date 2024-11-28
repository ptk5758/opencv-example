import pathlib
def getDocumentPath() -> str :
    return str(pathlib.Path.home().joinpath("Documents"))