def link_edit(a):
    b = "https://drive.google.com/uc?export=download&id=FILE_ID"
    c = a[32:]
    e = c[:-5]
    f = b[:-7]
    d = f+e
    return d
