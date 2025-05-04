user_string=input()
def one(string):
    polindrom=""
    collection_of_polindrom=[]
    for i in string:
        polindrom=i+polindrom
        if polindrom[::-1] in string:
            collection_of_polindrom.append(polindrom)
    return collection_of_polindrom[-1]     
print(one(user_string))
