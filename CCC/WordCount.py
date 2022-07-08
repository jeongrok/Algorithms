line = input()
wordcount = line.count(' ') + 1
print(wordcount)

class Weight():
    weight = 100

    # Defining a method
    def to_pounds(self):
        return 2.205 * self.weight

# Defining a function
def to_pounds(kilos):
    return 2.205 * kilos

# Calling a method on an object.
w = Weight()
pounds = w.to_pounds()

# Calling a function on an object
kilos = 100
pounds = to_pounds(kilos)