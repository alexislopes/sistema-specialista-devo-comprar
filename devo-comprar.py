from pyknow import *

class Devo(Fact):
    '''
    Informaçãoes para definir se devo ou não comprar

    variáveis
        amou: se você amou ou não do item em questão. [s/n]
        quer: se você realmente quer o item em questão. [s/n]
        serve: se o item é do seu tamanho. [s/n]
        troca: se você pode trocar este item. [s/n]
        sempre: se você irá usar este item de forma recorrente. [s/n]
        combina: se este item combina com algo. [s/n]
        parecido: se você já possui algo parecido. [s/n]
        usa: se você usa esta peça parecida. [s/n]
        especial: se este item é especial para você. [s/n]
        muito: se você possui muitos itens iguais a este. [s/n] 
    '''
    pass

class DevoComprar(KnowledgeEngine):

    @Rule(OR(Devo(parecido="n"), Devo(muito="n"), Devo(especial="s")))
    def comprar(self):
        print("\n\n\t> > > Vá com tudo, Compare! < < <\n\n")

    @Rule(OR(Devo(muito="s"), Devo(usa="n"), Devo(especial="n"), Devo(troca="n"), Devo(quer="n")))
    def nao_comprar(self):
        print("\n\n\t> > > Melhor deixar para depois! < < <\n\n")

    @Rule(Devo(usa="s"))
    def muito(self):
        self.declare(Devo(muito = input("\nVocê possiu muitos itens iguals a este? [s/n]")))

    @Rule(AND(Devo(parecido="s")))
    def usa(self):
        self.declare(Devo(usa=input("\nVocê usa com regularidade estes itens parecidos? [s/n]")))

    @Rule(OR(Devo(sempre="s"), Devo(combina="s")))
    def parecido(self):
        self.declare(Devo(parecido=input("\nVocê possui itens parecidos com o em questão? [s/n]")))

    @Rule(OR(Devo(serve="s"), Devo(troca="s")))
    def sempre(self):
        self.declare(Devo(sempre=input("\nVocê utilizará este item com regularidade? [s/n]")))

    @Rule(OR(Devo(amou="s"), Devo(quer="s")))
    def serve(self):
        self.declare(Devo(serve=input("\nEste item serve para você? [s/n]")))

    @Rule(AND(Devo(sempre="n")))
    def combina(self):
        self.declare(Devo(combina=input("\nEste item combina com você? [s/n]")))

    @Rule(AND(Devo(combina="n")))
    def especial(self):
        self.declare(Devo(especial=input("\nEste item tem um valor sentimental ou é especial para você? [s/n]")))

    @Rule(AND(Devo(serve="n")))
    def troca(self):
        self.declare(Devo(troca=input("\nHá possibilidade de troca? [s/n]")))

    @Rule(AND(Devo(amou="n")))
    def quer(self):
        self.declare(Devo(quer=input("\nVocê realmente quer este item? [s/n]")))


engine = DevoComprar()
engine.reset()

engine.declare(Devo(amou=input("\nVocê amou este item? [s/n]")))

engine.run()

