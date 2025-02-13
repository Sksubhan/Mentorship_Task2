def summation(a,b):
    if str(type(a))[-5:-2]=='str' or str(type(b))[-5:-2]=='str':
        return 'Please do not use string as input'
    else:
        return a+b
