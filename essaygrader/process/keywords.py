def keyWords(keyWords, essay):
    count = 0
    for i in keyWords:
        count += essay.count(i)
    result = round((count/len(essay)*100), 2)
    return result