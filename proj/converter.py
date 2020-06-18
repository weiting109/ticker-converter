from datetime import datetime

def split_bbticker(bbticker):
    """
    Given a Bloomberg ticker as a string, return:
    - string ticker prefix
    - string expiry month (mapped character)
    - string expiry year
    - string sector
    """

    running = "" # ticker and month
    for c in bbticker:
        if ord(c) < ord("0") or ord(c) > ord("9"):
            running+=c
        else: break
    prefix = running[:-1].rstrip()
    month_char = running[-1]

    bbticker = bbticker[len(running):] # remainder of string
    running = bbticker.split() # expiry year and sector separated by space
    year, sector = running[0], running[1]

    # resolving truncated years to expiry years
    currYear = datetime.now().year
    if len(year)==1:
        year = ''.join([str(currYear//10),year])
    else:
        year = ''.join([str(currYear//100),year])

    return prefix,month_char,year,sector

def generate_cusip8(bbticker):
    """
    Given a bloomberg ticker as a string, return a string of 8 alphanumeric
    characters (modified CUSIP without checkdigit).
    """
    prefix,month_char,year,_ = split_bbticker(bbticker)
    if len(prefix) == 1:
        cusip8 = "".join([prefix,month_char,year[-1],year,year[-1]])
    elif len(prefix) == 2:
        cusip8 = "".join([prefix,month_char,year[-1],year])
    else:
        cusip8 = "".join([prefix,month_char,year[-1],year[:-1]])

    return cusip8

def generate_cusip_checkdigit(cusip8):
    """
    Given an 8-alphanumeric character sting cusip8, return the check digit for
    modified CUSIP.
    """

    # algorithm approach
    sum = 0
    for i in range(8):
        c = cusip8[i]
        if c.isnumeric():
            v = int(c)
        else:
            p = ord(c)-ord('A')+1
            v = p+9
        if (i+1)%2 == 0: # if in even position
            v *= 2
        sum = sum + v//10 + v%10

    return (10 - (sum%10))%10

def convert():
    return void
