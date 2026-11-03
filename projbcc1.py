pacientes = [["Maria Silva", "111.222.333-44", "123", "98888-8888", "Nenhuma"]]
adms = [["admin", "123"]]
dentistas = [["1", "Dr. Carlos", "CRO123", "Ortodontia"], ["2", "Dra. Ana", "CRO456", "Endodontia"]]
consultorios = [["Sala 1", "Dr. Carlos"], ["Sala 2", "Dra. Ana"]]
consultas = []

while True:
    print("\n     ***** CLÍNICA ODONTOCLEAN *****")
    print(" 1 - Módulo Paciente")
    print(" 2 - Módulo Administração / Secretaria")
    print(" 0 - Encerrar Sistema")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("\n--- ACESSO AO PACIENTE ---")
        cpf_login = input("Digite o seu CPF: ")

        paciente_encontrado = False
        indice_paciente = 0

        while indice_paciente < len(pacientes):
            if cpf_login == pacientes[indice_paciente][1]:
                paciente_encontrado = True
                break
            indice_paciente += 1

        if paciente_encontrado:
            senha_login = input("Digite sua senha: ")
            if senha_login == pacientes[indice_paciente][2]:
                print(f"\nLogin efetuado com sucesso! Bem-vindo(a), {pacientes[indice_paciente][0]}")

                while True:
                    print("\n--- MENU DO PACIENTE ---")
                    print("1 - Ver Corpo Clínico")
                    print("2 - Agendar Consulta")
                    print("3 - Minhas Consultas")
                    print("4 - Cancelar Consulta")
                    print("0 - Sair da Conta")

                    op_pac = int(input("Escolha uma opção: "))

                    if op_pac == 1:
                        print("\n--- CORPO CLÍNICO DISPONÍVEL ---")
                        i = 0
                        while i < len(dentistas):
                            print(
                                f"ID: {dentistas[i][0]} | Nome: {dentistas[i][1]} | CRO: {dentistas[i][2]} | Especialidade: {dentistas[i][3]}")
                            i += 1

                    elif op_pac == 2:
                        print("\n--- AGENDAR CONSULTA ---")
                        i = 0
                        while i < len(dentistas):
                            print(f"- {dentistas[i][1]} ({dentistas[i][3]})")
                            i += 1

                        nome_dentista = input("Digite o nome do dentista desejado: ")
                        dentista_existe = False
                        i = 0
                        while i < len(dentistas):
                            if dentistas[i][1].lower() == nome_dentista.lower():
                                dentista_existe = True
                                nome_dentista = dentistas[i][1]
                                break
                            i += 1

                        if not dentista_existe:
                            print("Erro: Dentista não encontrado no catálogo! Não é possível prosseguir.")
                        else:
                            data = input("Digite a data desejada (DD/MM/AAAA): ")
                            horario = input("Digite o horário desejado (HH:MM): ")
                        data = input("Digite a data desejada (DD/MM/AAAA): ")
                        horario = input("Digite o horário desejado (HH:MM): ")

                        conflito = False
                        i = 0
                        while i < len(consultas):
                            if consultas[i][1] == nome_dentista and consultas[i][2] == data and consultas[i][
                                3] == horario:
                                conflito = True
                                break
                            i += 1

                        if conflito:
                            print("Erro: O dentista já possui consulta marcada neste horário!")
                        else:
                            consultas.append([pacientes[indice_paciente][1], nome_dentista, data, horario])
                            print("Consulta agendada com sucesso!")

                    elif op_pac == 3:
                        print("\n--- MINHAS CONSULTAS FUTURAS ---")
                        encontrou = False
                        i = 0
                        while i < len(consultas):
                            if consultas[i][0] == pacientes[indice_paciente][1]:
                                print(
                                    f"Dentista: {consultas[i][1]} | Data: {consultas[i][2]} | Horário: {consultas[i][3]}")
                                encontrou = True
                            i += 1
                        if not encontrou:
                            print("Nenhuma consulta encontrada para o seu CPF.")

                    elif op_pac == 4:
                        print("\n--- CANCELAR CONSULTA ---")
                        data_canc = input("Digite a data da consulta a cancelar (DD/MM/AAAA): ")
                        hor_canc = input("Digite o horário da consulta (HH:MM): ")

                        removido = False
                        i = 0
                        while i < len(consultas):
                            if consultas[i][0] == pacientes[indice_paciente][1] and consultas[i][2] == data_canc and \
                                    consultas[i][3] == hor_canc:
                                consultas.pop(i)
                                print("Consulta cancelada com sucesso!")
                                removido = True
                                break
                            i += 1
                        if not removido:
                            print("Consulta não encontrada com esses dados.")

                    elif op_pac == 0:
                        print("Saindo do ambiente do paciente...")
                        break
                    else:
                        print("Opção inválida.")
            else:
                print("Senha incorreta.")
        else:
            print("\nCPF não encontrado na base de dados.")
            resp = int(input("Deseja realizar seu auto-cadastro básico? (1 - Sim, 2 - Não): "))
            if resp == 1:
                nome = input("Digite seu nome completo: ")
                senha = input("Crie sua senha: ")
                telefone = input("Digite seu telefone: ")
                observacoes = "Nenhuma"
                pacientes.append([nome, cpf_login, senha, telefone, observacoes])
                print("Auto-cadastro realizado com sucesso! Faça o login novamente.")

    elif opcao == 2:
        print("\n--- ACESSO À ADMINISTRAÇÃO / SECRETARIA ---")
        login_adm = input("Digite o usuário ADM: ")
        senha_adm = input("Digite a senha ADM: ")

        adm_logado = False
        i = 0
        while i < len(adms):
            if login_adm == adms[i][0] and senha_adm == adms[i][1]:
                adm_logado = True
                break
            i += 1

        if adm_logado:
            print(f"\nLogin efetuado com sucesso! Bem-vindo(a), {login_adm}")

            while True:
                print("\n--- MENU DA ADMINISTRAÇÃO ---")
                print("1 - Gestão de Dentistas (CRUD)")
                print("2 - Gestão de Consultórios")
                print("3 - Gestão de Pacientes (CRUD Completo)")
                print("4 - Gestão da Agenda Geral")
                print("0 - Sair da Conta")

                op_adm = int(input("Escolha uma opção: "))

                if op_adm == 1:
                    while True:
                        print("\n--- GESTÃO DE DENTISTAS ---")
                        print("1 - Cadastrar Dentista")
                        print("2 - Listar Dentistas")
                        print("3 - Remover Dentista")
                        print("0 - Voltar")
                        op_dent = int(input("Escolha: "))

                        if op_dent == 1:
                            did = input("ID do dentista: ")
                            dnome = input("Nome: ")
                            dcro = input("CRO: ")
                            desp = input("Especialidade: ")
                            dentistas.append([did, dnome, dcro, desp])
                            print("Dentista cadastrado com sucesso!")
                        elif op_dent == 2:
                            i = 0
                            while i < len(dentistas):
                                print(
                                    f"ID: {dentistas[i][0]} | Nome: {dentistas[i][1]} | CRO: {dentistas[i][2]} | Esp: {dentistas[i][3]}")
                                i += 1
                        elif op_dent == 3:
                            did = input("Digite o ID do dentista a remover: ")
                            i = 0
                            removido = False
                            while i < len(dentistas):
                                if dentistas[i][0] == did:
                                    dentistas.pop(i)
                                    print("Removido com sucesso!")
                                    removido = True
                                    break
                                i += 1
                            if not removido:
                                print("Dentista não encontrado.")
                        elif op_dent == 0:
                            break

                elif op_adm == 2:
                    while True:
                        print("\n--- GESTÃO DE CONSULTÓRIOS ---")
                        print("1 - Cadastrar/Vincular Sala")
                        print("2 - Listar Consultórios")
                        print("0 - Voltar")
                        op_cons = int(input("Escolha: "))

                        if op_cons == 1:
                            sala = input("Nome/Número da Sala: ")
                            dentista_vinc = input("Nome do Dentista responsável: ")
                            consultorios.append([sala, dentista_vinc])
                            print("Consultório vinculado com sucesso!")
                        elif op_cons == 2:
                            i = 0
                            while i < len(consultorios):
                                print(f"Sala: {consultorios[i][0]} | Dentista: {consultorios[i][1]}")
                                i += 1
                        elif op_cons == 0:
                            break

                elif op_adm == 3:
                    while True:
                        print("\n--- GESTÃO DE PACIENTES ---")
                        print("1 - Listar Pacientes")
                        print("2 - Buscar por Nome ou CPF")
                        print("3 - Atualizar Dados e Inserir Observações/Alergias")
                        print("0 - Voltar")
                        op_gpac = int(input("Escolha: "))

                        if op_gpac == 1:
                            i = 0
                            while i < len(pacientes):
                                print(
                                    f"Nome: {pacientes[i][0]} | CPF: {pacientes[i][1]} | Tel: {pacientes[i][3]} | Obs: {pacientes[i][4]}")
                                i += 1
                        elif op_gpac == 2:
                            busca = input("Digite o Nome ou CPF: ")
                            i = 0
                            encontrou = False
                            while i < len(pacientes):
                                if busca in pacientes[i][0] or busca in pacientes[i][1]:
                                    print(
                                        f"Encontrado -> Nome: {pacientes[i][0]} | CPF: {pacientes[i][1]} | Tel: {pacientes[i][3]} | Obs: {pacientes[i][4]}")
                                    encontrou = True
                                i += 1
                            if not encontrou:
                                print("Nenhum paciente encontrado.")
                        elif op_gpac == 3:
                            cpf_busca = input("Digite o CPF do paciente para atualizar: ")
                            i = 0
                            atualizado = False
                            while i < len(pacientes):
                                if pacientes[i][1] == cpf_busca:
                                    pacientes[i][0] = input("Novo nome: ")
                                    pacientes[i][3] = input("Novo telefone: ")
                                    pacientes[i][4] = input("Adicionar observações/alergias: ")
                                    print("Dados atualizados com sucesso!")
                                    atualizado = True
                                    break
                                i += 1
                            if not atualizado:
                                print("Paciente não encontrado.")
                        elif op_gpac == 0:
                            break

                elif op_adm == 4:
                    while True:
                        print("\n--- GESTÃO DA AGENDA GERAL ---")
                        print("1 - Visualizar Agenda Completa")
                        print("2 - Cancelar Consulta de Paciente")
                        print("0 - Voltar")
                        op_ag = int(input("Escolha: "))

                        if op_ag == 1:
                            if len(consultas) == 0:
                                print("Não há consultas agendadas.")
                            else:
                                i = 0
                                while i < len(consultas):
                                    print(
                                        f"Paciente CPF: {consultas[i][0]} | Dentista: {consultas[i][1]} | Data: {consultas[i][2]} | Horário: {consultas[i][3]}")
                                    i += 1
                        elif op_ag == 2:
                            cpfc = input("CPF do paciente da consulta: ")
                            datac = input("Data (DD/MM/AAAA): ")
                            horc = input("Horário (HH:MM): ")
                            remv = False
                            i = 0
                            while i < len(consultas):
                                if consultas[i][0] == cpfc and consultas[i][2] == datac and consultas[i][3] == horc:
                                    consultas.pop(i)
                                    print("Consulta cancelada pela administração com sucesso!")
                                    remv = True
                                    break
                                i += 1
                            if not remv:
                                print("Consulta não encontrada.")
                        elif op_ag == 0:
                            break

                elif op_adm == 0:
                    print("Saindo do ambiente administrativo...")
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Login ou senha de administrador incorretos...")

    elif opcao == 0:
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")