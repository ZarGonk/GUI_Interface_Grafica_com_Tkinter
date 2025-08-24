from time import sleep

print('-- Calculadora de peso --\n')

name = str(input('Digite seu nome: ')) 
weight= float(input('Digite seu peso: '))

print('\n[', end='')
for i in range(20):
    print('#',end='',flush=True)
    sleep(0.2)
print(']  100%')

sleep(0.1)
print(f'\nOlá {weight} Kg seu peso é: {name}')