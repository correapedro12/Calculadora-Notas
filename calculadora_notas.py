fez_a_p1 = input('Você fez a P1? Responda [S]im ou [N]ão: ')
fez_a_p2 = input('Você fez a P2? Responda [S]im ou [N]ão: ')

if  (fez_a_p1 == "S" or fez_a_p1 == "s") and (fez_a_p2 == "S" or fez_a_p2 == "s"):
    nota_p1 = input("Digite sua nota da P1: ")
    nota_p2 = input("Digite sua nota da P2: ")
    try:
        nota_p1_float = float(nota_p1)
        nota_p2_float = float(nota_p2)
    except:
        print("Digite apenas números!")
        exit()
    media_p1_p2 = (nota_p1_float + nota_p2_float) / 2
    nota_para_tirar_na_pf = 10 - media_p1_p2
    if media_p1_p2 >= 7:
        print(f'Sua média é: {media_p1_p2}.')
        print('Parabéns, você foi aprovado(a)!')
    elif media_p1_p2 < 4:
        print(f'Sua média é: {media_p1_p2}.')
        print('Infelizmente sua média foi menor que 4 e você está reprovado(a).')
    else:
        print(f'Sua média é: {media_p1_p2}.')
        print('Sua média está entre 6.9 e 4, então deve fazer a Prova Final.')
        print(f'Para ser aprovado(a), você deverá tirar no mínimo {nota_para_tirar_na_pf:.2f} na Prova Final.')
elif (fez_a_p1 == "N" or fez_a_p1 == "n") and (fez_a_p2 == "N" or fez_a_p2 == "n"):
    print("Você não fez nenhuma prova!")
elif (fez_a_p1 == "N" or fez_a_p1 == "n") or (fez_a_p2 == "N" or fez_a_p2 == "n"):
    if (fez_a_p1 == "N" or fez_a_p1 == "n"):
        realizou_a_pr_sem_p1 = input('Já fez a Prova de Reposição? Responda [S]im ou [N]ão: ')
        if (realizou_a_pr_sem_p1 == "S" or realizou_a_pr_sem_p1 == "s"):
            nota_p2_fez_pr = input("Digite sua nota da P2: ")
            nota_pr_p1 = input("Digite sua nota da Prova de Reposição: ")
            try:
                nota_p2_fez_pr_float = float(nota_p2_fez_pr)
                nota_pr_p1_float = float(nota_pr_p1)
            except:
                print("Digite apenas números!")
                exit()
            media_p2_pr = (nota_p2_fez_pr_float + nota_pr_p1_float) / 2
            nota_para_tirar_na_pf_p2_pr = 10 - media_p2_pr
            if media_p2_pr >= 7:
                print(f"Sua média é: {media_p2_pr:.2f}.")
                print("Parabéns, você foi aprovado(a)!")
            elif media_p2_pr < 4:
                print(f"Sua média é: {media_p2_pr:.2f}.")
                print('Infelizmente sua média foi menor que 4 e você está reprovado(a).')
            else:
                print(f"Sua média é: {media_p2_pr:.2f}")
                print('Sua média está entre 6.9 e 4, então deve fazer a Prova Final.')
                print(f"Para ser aprovado(a), você deverá tirar no mínimo {nota_para_tirar_na_pf_p2_pr:.2f} na Prova Final.")
        elif (realizou_a_pr_sem_p1 == "N" or realizou_a_pr_sem_p1 == "n"):
            nota_p2_sem_pr = input("Digite sua nota da P2: ")
            try:
                nota_p2_sem_pr_float = float(nota_p2_sem_pr)
            except:
                print("Digite apenas números!")
                exit()
            nota_pr_para_p1 = 14 - nota_p2_sem_pr_float
            print(f"Para passar direto na matéria, você deverá tirar no mínimo {nota_pr_para_p1:.2f} na Prova de Reposição.")
        else:
            print("Resposta inválida. Por favor, responda [S]im ou [N]ão.")
    elif (fez_a_p2 == "N" or fez_a_p2 == "n"):
        realizou_a_pr_sem_p2 = input('Já fez a Prova de Reposição? Responda [S]im ou [N]ão: ')
        if (realizou_a_pr_sem_p2 == "S" or realizou_a_pr_sem_p2 == "s"):
            nota_p1_fez_pr = input("Digite sua nota da P2: ")
            nota_pr_p2 = input("Digite sua nota da Prova de Reposição: ")
            try:
                nota_p1_fez_pr_float = float(nota_p1_fez_pr)
                nota_pr_p2_float = float(nota_pr_p2)
            except:
                print("Digite apenas números!")
                exit()
            media_p1_pr = (nota_p1_fez_pr_float + nota_pr_p2_float) / 2
            nota_para_tirar_na_pf_p1_pr = 10 - media_p1_pr
            if media_p1_pr >= 7:
                print(f"Sua média é: {media_p1_pr:.2f}.")
                print("Parabéns, você foi aprovado(a)!")
            elif media_p1_pr < 4:
                print(f"Sua média é: {media_p1_pr:.2f}.")
                print('Infelizmente sua média foi menor que 4 e você está reprovado(a).')
            else:
                print(f"Sua média é: {media_p1_pr:.2f}.")
                print('Sua média está entre 6.9 e 4, então deve fazer a Prova Final.')
                print(f"Para ser aprovado(a), você deverá tirar no mínimo {nota_para_tirar_na_pf_p1_pr:.2f} na Prova Final.")
        elif (realizou_a_pr_sem_p2 == "N" or realizou_a_pr_sem_p2 == "n"):
            nota_p1_sem_pr = input("Digite sua nota da P1: ")
            try:
                nota_p1_sem_pr_float = float(nota_p1_sem_pr)
            except:
                print("Digite apenas números!")
                exit()
            nota_pr_para_p2 = 14 - nota_p1_sem_pr_float
            print(f"Para passar direto na matéria, você deverá tirar no mínimo {nota_pr_para_p2:.2f} na Prova de Reposição.")
        else:
            print("Resposta inválida. Por favor, responda [S]im ou [N]ão.")
    else:
        print("Resposta inválida. Por favor, responda [S]im ou [N]ão.")
else:
    print("Resposta inválida. Por favor, responda [S]im ou [N]ão.")