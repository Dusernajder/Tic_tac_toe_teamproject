class Color():
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    MAGENTA = lambda x: '\033[35m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    RED = lambda x: '\033[31m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)



