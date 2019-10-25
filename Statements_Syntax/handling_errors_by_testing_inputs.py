while True:
    reply = input('Enter text:\n >>> ')
    if reply == 'exit':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Byeeee')
