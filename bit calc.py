
# functions go here

# text is what you want to say and deco is the deco
def statement(text, deco):
    
    # makes a string with 5 repeats
    end = deco * 5

    # add deco
    statement = "{} {} {}".format(end, text, end)

    print("")
    print(statement)
    print("")

    return ""

# main rotuine 

statement("Hello there", "[]")