
def object_name(obj, ret=None):
    g=globals()
    ret=[]
    obj_id=id(obj)
    for i in g.keys() :
        if id(g[i]) == obj_id :
            # print "msg1", i, g[i]
            ret.append(i)
    return ret


def rl (mylist=None, prefix=None, limit=7):
    prefix = prefix if prefix else "l"
    limit = limit if limit else 7

    aux=list(Out.keys()) # we want to make a copy
    aux.sort()
    aux.reverse()
    last_index = aux[0]

    if mylist == None :
        mylist = Out[last_index]
        mylist_name=In[last_index]

        if type(mylist) is not  list :
            for i in aux :
                # print "msg2", i, Out[i],
                if type(Out[i]) is list :
                    mylist = Out[i]
                    mylist_name=In[i]
                    print("using last list object: %s" % mylist_name)
                    break
    else :
        mylist_name = filter( lambda x: not x.startswith("_"), object_name(mylist))

    if type(mylist) is not  list :
        print("can't find any list or specified object is not a list")
        return

    glo=globals()

    for k, val in enumerate(mylist) :
        if k <= limit :
            name=prefix+str(k)
            glo[name]=val
            print("created variable %s = %s" % (name, val) )
        else :
            print("list %s has %d elements but only 7 was printed" % ( mylist_name, len(mylist) ) )
            break

def rla (**kargs) :
    rl(prefix="a", **kargs)

def rlb (**kargs) :
    rl(prefix="b", **kargs)

print
print("auxiliary functions `rl` `rla` and `rlb` have been defined")
