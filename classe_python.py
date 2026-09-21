#criação de classe

class VEICULO:
    #metodo construtor - ele é chamado automaticamente toda a vez 
    # que eu instacio (crio) um objeto da classe.
    def __init__(self, marca, modelo, cor, ano, motor = "motor padrão"):
        #caso coloque dois _ por exemplo __marca, ele se torna 
        # um atributo privado, ou seja, não pode ser acessado
        # fora da classe. E não pode ser alterado fora da classe.
        # ou altera direto por aqui ouu criar um metodo (def) para alterar
        # o valor do atributo e velo.
        self.marca              = marca
        self.modelo             = modelo
        self.cor                = cor
        self.ano                = ano
        self.velocidade         = 0
        self.__motor            = motor
    def obter_motor(self): # esse vc consegue ver o valor do atributo priv
     return self.__motor
 
    def alterar_motor(self, novo_motor): # esse vc consegue alterar o valor do atributo priv
        self.__motor = novo_motor

    # metodo da classe - são as operações/ funções que podem ser 
    #realizadas pelos objetos da classe.
    def acelerar(self):
        self.velocidade += 10
        return f"A velocidade atual é: {self.velocidade} km/h"
    
    def obter_velocidade(self):
        return f"A velocidade atual é: {self.velocidade} km/h"  
    
    def frear(self):
        if self.velocidade > 10:
            self.velocidade -= 10
            return f"A velocidade atual é: {self.velocidade} km/h"
        
        return "O veículo já está parado."
class Carro(VEICULO):
    def __init__(self, marca, modelo, cor, ano, num_portas, volume_porta_malas):
        super().__init__(marca, modelo, cor, ano)
        self.num_portas = num_portas
        self.volume_porta_malas = volume_porta_malas
        self.numero_rodas = 4
    
    def buzinar(self):
        return "Buzinando: Beep Beep!"
    
class Moto(VEICULO):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
        self.numero_rodas = 2
    
    def empinar(self):
        return "Empinando a moto!"
    def buzinar(self):
        return "Buzinando: Biiiiiiip!"

meu_poize = VEICULO("Honda", "Civic", "Prata", 2020)
meu_carro = Carro("Toyota", "Corolla", "Branca", 2021, 4, 500)
minha_moto = Moto("Yamaha", "MT-07", "Vermelha", 2022)
meu_poize.alterar_motor("Motor turbo do Relampago Marquinhos")


while (minha_moto.velocidade < 100):
    print('randadandandannnnn')
    minha_moto.acelerar()
    
for x in range(10):
    meu_poize.acelerar()

print('\nVelocidade da Moto:', minha_moto.obter_velocidade())
print('\nVelocidade do Civic:', meu_poize.obter_velocidade())
print('\nMotor do Civic:', meu_poize.obter_motor())
print("\n (Carro",meu_carro.buzinar(),')')
print("\n (Moto",minha_moto.buzinar(),')')
print("\n (Moto:",minha_moto.empinar(),')')
