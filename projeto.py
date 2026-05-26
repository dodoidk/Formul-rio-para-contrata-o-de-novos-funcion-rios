print('Bem vindo a empresa Nexct! A seguir preencha as informações para concorrer a vaga, Boa sorte')
while True:
    nome = input('Digite seu nome completo sem abreviações: ')
    if nome.isalpha():
        break
    else:
        print('Tente novamente, apenas letras')
while True:
    idade = str(input('Digite sua idade somente números: '))
    if idade.isdigit():
        break
    else:
        print('Tente novamente, apenas números.')
while True:
    cpf = str(input('Digite seu CPF completo, somente números: '))
    if cpf.isdigit():
        break
    else:
        print('Tente novamente, apenas números.')
while True:        
    dif = input('Qual seu diferencial que agregaria na vaga que está concorrendo?: ')
    if dif.isalpha():
        break
    else:
        print('Tente novamente, apenas letras')
while True:        
    motivo = input('Porque deveriamos te contratar?: ')
    if motivo.isalpha():
        break
    else:
        print('Tente novamente, apenas letras')
while True:        
    experiencia = input('Fale breviamente sobre suas experiências profissionais ao longo de sua carreira no mercado de trabalho: ')
    if experiencia.isalpha():
        break
    else:
        print('Tente novamente, apenas letras')
        
print('Obrigado por preencher as informações, aguarde o retorno da empresa via email! ')
