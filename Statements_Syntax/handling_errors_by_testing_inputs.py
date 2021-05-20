while True:
    reply = input('Enter text:\n >>> ')
    if reply == 'exit':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Byeeee')


def sum_int(a, b):
    return a + b

a = 4
b = 6

print(sum_int(a, b))