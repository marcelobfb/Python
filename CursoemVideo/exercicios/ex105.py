def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    estudante = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if estudante['média'] >= 7:
            estudante['situação'] = 'APROVADO'
        elif estudante['média'] >= 5:
            estudante['situação'] = 'RECUPERAÇÃO'
        else:
            estudante['situação'] = 'REPROVADO'
    return estudante


# programa principal
resp = notas(6.9,6.9,7.5, sit=True)
print(resp)
