'''
CtC 1.6 String Compression
15/12/2016

'''
def compress_string(the_string):
    l = list(the_string)
    r = [l[0],1]
    index = 1

    while index < len(the_string):
        if l[index] == l[index-1]:
            r[-1] = r[-1] + 1
        else:
            r.append(l[index])
            r.append(1)
        index += 1

    if len(r) < len(the_string):
        # gotcha : doesn't like if you don't handle the int's in the list : so iterate and cast
        return "".join(str(x) for x in r)
    return the_string

def test_wrapper(the_string):
    print("%s -> %s" % (the_string, compress_string(the_string)))

test_wrapper("aabcccccaaa")
test_wrapper("abcdefg")



