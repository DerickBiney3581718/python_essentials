def outer(par):
    loc = par
    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())
# ^ function(copy that maintains its store) returned from the invocation 