import os


def pdf(filename):
    y = "ppt2pdf file "+filename
    t = 'cmd /c "'+y+'"'
    return os.system(t)
