personagem = []

def cadastrar_personagem():
    nome = str(input('Digite o nome do personagem: '))
    nivel = int(input('Digite o nível do personagem: '))
    habilidade = str(input('Qual será a habilidade o personagem: '))
    classe = str(input('Qual será a classe do personagem: '))

    personagens = {'nome': nome,
                   'nível': nivel,
                   'habilidade': habilidade,
                   'classe': classe}

    personagem.append(personagens)
    print('😁Personagem cadastrada com sucesso!😁 \n')

def buscar_personagem():
    termo = str(input('Digite o nome ou a classe do personagem para fazer a busca: ')).lower()
    encontrado = []
    for personagens in personagem:
        if (termo in personagens['nome'].lower()) or (termo in personagens['classe'].lower()):
            encontrado.append(personagens)

    if len(encontrado) == 0:
        print('😣 Nenhum personagem cadastrado 😣\n')
        return
    print(encontrado)

def tabela_personagem():
    if len(personagem) == 0:
        print('😣 Nenhum personagem cadastrado 😣\n')
        return
    numero = 1
    for personagens in personagem:
        print(f'[{numero}] nome: {personagens['nome']} | nível: {personagens['nível']} |'
              f' habilidade: {personagens['habilidade']} | classe: {personagens['classe']}')
        numero += 1
    print()

def editar_personagem():
    if len(personagem) == 0:
        print('😣Nenhum personagem encontrado😣 \n')
        return
    else:
        tabela_personagem()
        numero = int(input('Digite o numero do personagem para editá-lo: '))
        indice = numero - 1
        if numero <= len(personagem):
            novo_nivel = int(input('Digite o novo nível do personagem: '))
            nova_habilidade = str(input('Digite a nova habilidade do personagem: '))
            personagem[indice]['Nível'] = novo_nivel
            personagem[indice]['Habilidade'] = nova_habilidade
            print('✅Personagem editado com sucesso! ✅ \n')

def excluir_personagem():
    if len(personagem) == 0:
        print('😣Nenhum personagem encontrado😣 \n')
        return
    else:
        tabela_personagem()
        numero = int(input('Digite o numero do personagem para exclui-lo: '))
        indice = numero - 1
        if numero <= len(personagem):
            removido = personagem.pop(indice)
            print('✅personagem excluído com sucesso✅')

def menu_sistema():
    while True:
        print('==== RPG ORGANIZER ====')
        print('1. ✍️ Cadastrar personagem ✍️')
        print('2. 📝 Editar personagem 📝')
        print('3. 🔍 Buscar personagem 🔍')
        print('4. 📋 Tabela dos personagens 📋')
        print('5. 🗑️ Excluir personagem 🗑️')
        print('6. 🟥 Sair 🟥')
        escolha = str(input('Escolha uma opção: '))
        if escolha == '1':
            cadastrar_personagem()
        elif escolha == '2':
            editar_personagem()
        elif escolha == '3':
            buscar_personagem()
        elif escolha == '4':
            tabela_personagem()
        elif escolha == '5':
            excluir_personagem()
        elif escolha == '6':
            print('Saindo do sistema. Até mais!')
            break
        else:
            print('⚠️ Opção inválida! Tente novamente!')