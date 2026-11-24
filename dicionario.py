#Treino de vocabulário - Jogo
import random
dicionario = {
    "Que dura pouco tempo; passageiro ou transitório." : "Efêmero",
    "Capacidade de se colocar no lugar de outra pessoa e sentir o que ela sente." : "Empatia",
    "Algo que faz parte da essência ou natureza de algo; inseparável." : "Inerente",
    "Que age com ordem, cuidado e atenção aos detalhes." : "Metódico",
    "Que é próprio ou característico de alguém ou algo; singular." : "Peculiar",
    "Firmeza e constância para alcançar um objetivo, mesmo diante de dificuldades." : "Perseverança",
    "Que tem percepção rápida, aguda e inteligência para notar detalhes." : "Perspicaz",
    "Que fala ou escreve usando palavras demais, de forma longa e pouco objetiva." : "Prolixo",
    "Capacidade de se adaptar e recuperar-se bem diante de adversidades." : "Resiliência",
    "Astuto, esperto, com facilidade para entender situações ou intenções." : "Sagaz",
    "Descoberta feliz, valiosa ou interessante feita por acaso." : "Serendipidade",
    "Que eleva o espírito; de beleza ou grandeza extraordinária." : "Sublime",
    "Expressão de alegria por uma boa notícia recebida ou recompensa dada a quem traz novidades." : "Alvíssaras",
    "Estado de profundo encantamento, admiração ou êxtase diante de algo belo." : "Enlevo",
    "Aquilo que é tão grandioso, belo ou intenso que não pode ser descrito com palavras." : "Inefável",
    "Que demonstra fraqueza, abatimento ou uma melancolia suave e sonhadora." : "Lânguido",
    "O cheiro característico e agradável que sobe da terra seca quando começa a chover." : "Petricor",
    " Conversa que uma pessoa tem consigo mesma em voz alta, como uma reflexão solitária" : "Solilóquio",
    "Algo muito difícil de compreender, obscuro ou confuso." : "Abstruso",
    "Característica filosófica daquilo que existe por si mesmo, sem depender de outra causa." : "Asseidade",
    "Algo que causa dano, prejudica ou destrói lentamente." : "Algo que causa dano, prejudica ou destrói lentamente.",
}

tentativas = int(input("Digite quantas questões pretende fazer:  "))
pontos = 0

for t in range(tentativas):
    pergunta = random.choice(list(dicionario))
    resposta = input(f'Qual palavra melhor define "{pergunta}"? ')

    if resposta.strip().lower() == dicionario[pergunta].lower():
        print("Correto!")
        pontos += 1
    else:
        print(f"Errado! A resposta certa é {dicionario[pergunta]}.")

print(f"Você chegou ao fim do simulado! Você possui {pontos}/{tentativas} respostas corretas.")