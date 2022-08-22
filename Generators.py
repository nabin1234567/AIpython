def myrange( start, stop, step=1):
    assert step> 0
    i = start
    while i< stop:
        yield i
        i+= step

print(" list ( my range(2,30,3):",list(myrange(2,30,3)))