def sf1():  #static function 1 for testing the cl
    print("Invoked from a dynamic structure")

# main function ref structure AKA Mapper
dict = {
    "Invoke1": sf1
}

#Control layer for invoking from mapper
def cl(ck):
    dict[ck]()

#dynamic function handler for mappiung functions to keys
def dfh(fn, fnk):
    dict[fnk] = fn

cl("Invoke1") #test the static function invoke

#dynamic function 1 to be passed to the control layer
def df1():{
    print("Woowo this is from a dynamic function")
}

dfh(df1, "Invoke2")
cl("Invoke2")