def acronym(string):
    string = string.split()
    acr = ''
    for i in string:
        acr += i[0].upper()
    return acr
