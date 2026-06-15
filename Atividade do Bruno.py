personagem_rpg = []

def cadastrar_personagem():
    nome = str(input('Digite o nome do personagem: '))
    nivel = int(input('Digite o nível do personagem: '))
    habilidade = str(input('Qual será a habilidade do personagem: '))
    classe = str(input('Qual será a classe do personagem: '))

    personagens_rpg = {'nome': nome,
                   'nível': nivel,
                   'habilidade': habilidade,
                   'classe': classe}

    personagem_rpg.append(personagens_rpg)
    print('😁Personagem cadastrada com sucesso!😁 \n')

def buscar_personagem():
    termo = str(input('Digite o nome ou a classe do personagem para fazer a busca: ')).lower()
    cadastrado = []
    for personagens_rpg in personagem_rpg:
        if (termo in personagens_rpg['nome'].lower()) or (termo in personagens_rpg['classe'].lower()):
            cadastrado.append(personagens_rpg)

    if len(cadastrado) == 0:
        print('😣 Nenhum personagem cadastrado 😣\n')
        return
    print(cadastrado)

def tabela_personagem():
    if len(personagem_rpg) == 0:
        print('😣 Nenhum personagem cadastrado 😣\n')
        return
    numero = 1
    for personagens_rpg in personagem_rpg:
        print(f'[{numero}] nome: {personagens_rpg['nome']} | nível: {personagens_rpg['nível']} |'
              f' habilidade: {personagens_rpg['habilidade']} | classe: {personagens_rpg['classe']}')
        numero += 1
    print()

def editar_personagem():
    if len(personagem_rpg) == 0:
        print('😣Nenhum personagem encontrado😣 \n')
        return
    else:
        tabela_personagem()
        numero = int(input('Digite o numero do personagem para editá-lo: '))
        indice = numero - 1
        if numero <= len(personagem_rpg):
            novo_nivel = int(input('Digite o novo nível do personagem: '))
            nova_habilidade = str(input('Digite a nova habilidade do personagem: '))
            personagem[indice]['nivel'] = novo_nivel
            personagem[indice]['habilidade'] = nova_habilidade
            print('✅Personagem editado com sucesso! ✅ \n')

def excluir_personagem():
    if len(personagem_rpg) == 0:
        print('😣Nenhum personagem encontrado😣 \n')
        return
    else:
        tabela_personagem()
        numero = int(input('Digite o numero do personagem para exclui-lo: '))
        indice = numero - 1
        if numero <= len(personagem_rpg):
            removido = personagem_rpg.pop(indice)
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

menu_sistema()