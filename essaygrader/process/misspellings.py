# misspellings in the essay
# extra comment
def nmisspelled(essay):
    import enchant
    d = enchant.Dict("en_US")
    return sum([1 for word in essay if not d.check(word)])