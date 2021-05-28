import random
import string

tamanho = int(input('Digite o numero de caracteres que sua senha vai ter: '))

chars = string.ascii_letters + string.digits + '!@#$%*()-=+,.;:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))