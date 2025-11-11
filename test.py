class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade
        self.running = False
        self.eating = False


    def run(self):
        if self.running:
            print("it's Already running")
        elif not self.eating:
            self.running = True
            print('Run')
        else:
            self.running = False
            print('You cant run, you are eating')

    def stop_run(self):
        self.running = False
        print('Stopped Running')
    

    def eat(self):
        if self.eating:
            print("it's already eating")
        elif not self.running:
            self.eating = True
            print('Eating')
        else:
            self.eating = False
            print('You cant eat, you are running')
        
    def stop_eat(self):
        self.eating = False
        print('Stopped eating')
    

andry = Pessoa(1.58, 23)
andry.run()
andry.eat()
andry.run()
andry.stop_run()
andry.eat()
andry.eat()
andry.stop_eat()
