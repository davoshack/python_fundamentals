import ipdb;


B = '1101'
I = 0
while B != '':
    ipdb.set_trace()
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
