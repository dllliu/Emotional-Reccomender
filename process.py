def do(filename,extra):
    f = open(filename)
    f = f.read()
    arr = []
    for i in f.split("\n"):
        temp = "(" + i + ", \"" + extra + "\")"
        arr.append(temp)
    return arr
    

#temp = (do("a.txt","Sadness") + do("amger.txt","Anger") + do("Disgust.txt","Disgust") + do("Fear.txt","Fear") + do("Joy.txt","Joy") + do("loneliness.txt","loneliness") + do("Remorse.txt","Remorse") + do("Trust.txt","Trust"))
print(do("a.txt","Sadness"))