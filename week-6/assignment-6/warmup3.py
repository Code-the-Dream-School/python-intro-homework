def favorite_hobby():
    hobby = "hiking"
    return hobby    #return allows the value in that variable to be used. No return means the function just holds it

#print(hobby)    #NameError: name 'hobby' is not defined (return brings it forth so a variable outside the function can use it)
hobby = favorite_hobby()
print(hobby)
