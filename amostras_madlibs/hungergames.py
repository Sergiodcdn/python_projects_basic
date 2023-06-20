def madlib():
    number = input("Numero: ")
    adj = input("Adjetivo: ")
    verb = input("Verbo: ")
    verb2 = input("Verbo: ")
    noun = input("Substantivo: ")
    noun2 = input("Substantivo: ")
    noun3 = input("Substantivo: ")
    noun4 = input("Substantivo: ")
    noun5 = input("Substantivo: ")
    noun_plural = input("Substantivo (plural): ")
    noun_plural_2 = input("Substantivo (plural): ")
    noun_plural_3 = input("Substantivo (plural): ")
    sound_important = input("Algum nome que soe importante!: ")


    madlib=f"{number} segundos. É quanto tempo precisamos para {verb} em nossos círculos de metal antes do \
    som de um {noun} nos libertar. Saia antes que os {number} segundos acabem e {noun_plural} exploda suas \
    pernas fora. {number} segundos para entrar no anel de tributos todos equidistantes do {sound_important}, um gigante \
    {adj} {noun2} em forma de {noun3} com uma cauda curvada, cuja boca tem pelo menos 6 metros \
    alto, transbordando com as coisas que nos darão vida aqui na arena. Alimentos, água, \
    {noun_plural_2}, remédios, roupas, {noun_plural_3}. Espalhados pelo {sound_important} estão outros suprimentos, seu valor \
    diminuindo quanto mais longe eles estão do {noun2}. Por exemplo, a apenas alguns passos de meus pés está um metro \
    quadrado de {noun4}. Certamente poderia ser de alguma utilidade em um aguaceiro. Mas lá na boca, vejo um {noun5} \
    que protegeria de quase qualquer tipo de clima. Se eu tivesse coragem de entrar e {verb2} a favor contra \
    os outros vinte e três tributos. O que fui instruído a não fazer."
    
    print(madlib)

if __name__ == '__main__':
    madlib()