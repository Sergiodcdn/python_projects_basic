def madlib():
    time_of_day = input("Periodo do dia: ")
    body_part_plural = input("Parte do corpo (plural): ")
    color = input("Cor: ")
    verb_past_tense = input("Verbo (no passado): ")
    food = input("Comida: ")
    noun1 = input("Substantivo: ")
    noun_plural_1 = input("Substantivo (plural): ")
    adj1 = input("Adjetivo: ")
    adj2 = input("Adjetivo: ")
    adj3 = input("Adjetivo: ")


    madlib = f"Era um verão {adj1}, {time_of_day} quando percebemos que a vacina pararia \
    não tivemos o fim da doença. Em vez disso, produziu ZUMBIS!!! Eles estavam com sede de {body_part_plural} \
    e as ruas estavam repletas desses monstros segurando {noun_plural_1} em suas mãos. \
    Seus olhos estavam {color}, famintos, enquanto eles {verb_past_tense} ao redor da cidade procurando por {food}. \
    Eles eram {adj2} e {adj3}, sem saber como agir neste mundo humano... exceto comer {body_part_plural}!!!! \
    Essa era sua única missão e eles se dedicaram a alcançá-la pelo bem do {noun1}."
   
    print(madlib)