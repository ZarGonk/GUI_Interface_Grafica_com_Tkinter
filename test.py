def show_count(start=0, end=0, move=0):
    try:
        one = int(start)
        two   = int(end)
        three  = int(move)

        for i in range(one, two, three):
            print(i)
    except:
        print('Valor Invalido')
    

show_count('bom dia', 10+1, 2)  