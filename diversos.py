import datetime

import pyautogui as cursor
from time import sleep
from PIL import ImageGrab
from datetime import date
import clipboard

import os
global qt
tem_pendencia = False


menu_def = [['&Menu'],
            ['&Carta', ['&Citação', ['&Comum','&Citação e Notificação'],['&Intimação']]],
            ['&Malote',['&Devolução de CP via Malote','&Envio de CP para distribuição via Malote','&Envio de Ofício via Malote']],
            ['&Ajuda', ['&Sobre Requisitos gerais da aplicação','&Sobre e-mail SCPC','&Sobre Carta...']]

    ]

# Função para imprimir email enviado
def imp_email_enviado():
    usu = get_user()
    sleep(1.5)
    get_image('enviados', 4, 85, 250, 215, 450)
    sleep(2)
    cursor.click(350, 350)
    sleep(2)
    cursor.click(1010, 350)
    sleep(1)
    for i in range(10):
        cursor.scroll(400)
        sleep(0.2)

    #get_image('image2', 4)
    get_image('tres_pt_vermelho', 4, 900, 230, 120, 400)
    sleep(1)
    get_image('imp', 4, 750, 430, 200, 300)
    sleep(2)
    get_image('imp1', 4, 26, 110, 300, 400)
    sleep(3)
    get_image('imp2', 9, 20, 490, 300, 250)
    sleep(6)
    cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\1.pdf')
    sleep(0.5)
    cursor.press('enter')
    sleep(1)
    cursor.press('s')
    sleep(2)
    #get_image('cancelar', 4)
    get_image('fechar_email', 4, 130, 130, 250, 250)
    sleep(2)
    get_image('min_browser', 4, 800, 1, 150, 80)
    sleep(2)

    #get_image('min_aplicacao', 4, 750, 200, 300, 200)


# função para buscar os arquivos salvos na pasta Emails e anexar ao email
def anexar(qt):
    usu = get_user()
    i = 1
    while (i <= qt):
        get_image('anexar', 4, 718,150, 300, 200)
        sleep(1)
        get_image('neste_pc', 4, 350, 180, 600, 400)
        sleep(5)
        cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\anexo{i}.pdf')
        sleep(2)
        get_image('abrir', 4, 350, 320, 300, 400)
        sleep(2.5)
        i += 1
    get_image('tres_pt_cinza', 4, 850, 150, 150, 450)
    sleep(1)
    cursor.click(1010, 550)
    sleep(1)
    for i in range(10):
        cursor.scroll(-400)
        sleep(0.2)
    get_image('opcoes', 4, 650, 600, 350, 350)
    sleep(0.5)
    (aux_x, aux_y) = get_pos_image('conf_leitura', 4)
    cursor.click(aux_x, aux_y)
    sleep(0.5)
    cursor.click(aux_x, aux_y + 30)
    get_image('ok', 4, 450, 220, 300, 400)
    sleep(2)


# função para buscar o arquivo senha de acesso salvo na pasta Emails
def anexar_senha(np):
    usu = get_user()
    get_image('anexar', 4, 718,150, 300, 200)
    sleep(1)
    get_image('neste_pc', 4, 350, 180, 600, 400)
    #cursor.click(890, 250)
    #sleep(1)
    #cursor.click(700, 170)
    sleep(5)
    cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\Senha de acesso - {np}.pdf')
    sleep(2)
    get_image('abrir', 4, 350, 320, 300, 400)
    #cursor.click(500, 450)
    sleep(3)

# função para buscar o ofício salvo na pasta Emails
def anexar_oficio(np):
    usu = get_user()
    get_image('anexar', 4, 718,150, 300, 200)
    sleep(1)
    get_image('neste_pc', 4, 350, 180, 600, 400)
    #cursor.click(890, 250)
    #sleep(1)
    #cursor.click(700, 170)
    sleep(5)
    cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\Oficio - {np}.pdf')
    sleep(2)
    get_image('abrir', 4, 350, 320, 300, 400)
    sleep(3)


def btn_enviar():
    get_image('enviar', 4)


# captura o estado da tecla capslock
def get_capslock_state():
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


#captura o usuario logado
def get_user():
    return os.getenv('USER', os.getenv('USERNAME', 'user'))



# procura imagem na tela, clicando quando achar
def get_image(name_img, qtd_search, left, top, width, height, pause_yes= 0.5, pause_no= 1):
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/{name_img}.png', confidence=0.8, region=(left, top, width, height)):
            pos_x, pos_y = cursor.locateCenterOnScreen(f'assets/{name_img}.png', confidence=0.8, region=(left, top, width, height))
            sleep(pause_yes)
            cursor.click(pos_x, pos_y)
            #cursor.click(f'assets/{name_img}.png')#aqui no click nao pode ter confidence
            print(f'encontrei {name_img} na {cont + 1} vez.')
            break
        else:
            sleep(pause_no)
            print(f'nao encontrei {name_img} na {cont + 1} vez')
            cont += 1
            if cont == int(qtd_search):
                print(f'Chegou a {qtd_search} vez. Esse foi o limite estipulado')
                resp = cursor.confirm(f'Procurei a imagem "{name_img}.png" por {qtd_search} vezes, sem sucesso!  Deseja \n continuar? Se sim, primeiro minimize esta caixa de mensagem.\n Depois procure na tela e clique na imagem "{name_img}.pdf", e, por fim, restaure essa caixa e clique em "SIM"','Pergunta',buttons=('Sim', 'Não', 'Cancelar'))
                if resp == 'Sim':
                    break
                else:
                    print('Escolheu nao, então encerrei a aplicação.')
                    exit()


#verifica a existencia de uma imagem, trazendo a resposta como v ou f
def exists_image(name_img, qtd_search, left, top, width, height, pause_yes= 0.5, pause_no= 1):
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/{name_img}.png', confidence=0.8, region=(left, top, width, height)):
            resposta='v'
            sleep(pause_yes)
            print(f'achei {name_img} na {cont + 1} vez.')
            break
        else:
            sleep(pause_no)
            print(f' NÃO achei {name_img} na {cont + 1} vez.')
            cont += 1
            if cont == int(qtd_search):
                print(f'chegou a {qtd_search} vez. Foi o limite estipulado')
                resposta = 'f'
                break
                #exit()
    return (resposta)


# procura imagem na tela, capturando suas posições x, y quando a encontra
def get_pos_image(name_img, qtd_search, left, top, width, height, pause_yes= 0.5, pause_no= 1):
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/{name_img}.png', confidence=0.8, region=(left, top, width, height)):
            pos_x, pos_y = cursor.locateCenterOnScreen(f'assets/{name_img}.png', confidence=0.8, region=(left, top, width, height))
            sleep(pause_yes)
            print(pos_x, pos_y)
            break
        else:
            sleep(pause_no)
            cont += 1
            if cont == int(qtd_search):
                print(f'chegou a {qtd_search} vez. Foi o limite estipulado')
                resp = cursor.confirm(f'Procurei a imagem "{name_img}.png" por {qtd_search} vezes, sem sucesso! Por isso não sei sua posição.\n  Deseja  continuar? Se sim, primeiro minimize esta caixa de mensagem.\n Depois ative a tela que tem a imagem "{name_img}.pdf", e, por fim, restaure essa caixa e clique em "SIM"','Pergunta',buttons=('Sim', 'Não'))
                if resp == 'Sim':
                    pos_x, pos_y = cursor.locateCenterOnScreen(f'assets/{name_img}.png')
                    break
                else:
                    print('Escolheu nao, então encerrei a aplicação.')
                    exit()
    return (pos_x, pos_y)


def digitalizar(numero_processo, tipo_documento, nome_arquivo):
    usu = get_user()
    sleep(2)
    aux = numero_processo
    aux1 = aux.replace("-", "")
    aux2 = aux1.replace(".", "")
    num_aux = aux2[0:13]
    #cursor.click(1015, 500)
    get_image('digitalizacao',  4, 5, 5, 250, 300)
    sleep(4)
    cursor.hotkey('alt', 'l')
    (aux_x, aux_y) = get_pos_image('processo', 4, 3, 20, 200, 250)
    cursor.click(aux_x, aux_y + 18)
    sleep(0.5)
    cursor.write(num_aux)
    sleep(1)
    cursor.hotkey("tab")
    sleep(0.3)
    cursor.hotkey("tab")
    sleep(0.3)
    cursor.hotkey('alt', 'c')
    sleep(1)
    finalize_confirmacao(2)
    sleep(2)
    finalize_aviso(2)
    sleep(2)
    finalize_pendencias(3)
    (aux_x, aux_y) = get_pos_image('nova_peca', 4, 20, 50, 300, 300)
    cursor.click(aux_x - 23, aux_y)
    sleep(2)
    cursor.click(aux_x - 23, aux_y + 30)
    sleep(2)
    cursor.click(aux_x, aux_y)
    sleep(2.5)
    cursor.hotkey('left')
    sleep(1)
    cursor.write(tipo_documento)
    sleep(1)
    cursor.hotkey('enter')
    sleep(2)
    cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\{nome_arquivo}.pdf')
    sleep(0.5)
    cursor.hotkey('enter')
    sleep(2)
    #acho que o salvar deve ser  aqui
    #(aux_x, aux_y) = get_pos_image('pecas_agu_liberacao', 4)
    #cursor.click(aux_x + 15, aux_y + 35)
    #sleep(3)
    #cursor.hotkey('ctrl', 'j')
    #sleep(4)
    #cursor.hotkey('alt', 'l') liberar

def abrir_processo(numero_processo):
    #num_aux =""
    aux = numero_processo
    aux1 = aux.replace("-","")
    aux2 = aux1.replace(".","")
    num_aux = aux2[0:13]
    sleep(2)
    get_image('fluxo', 5, 5, 10, 200,200)
    sleep(2)
    if(exists_image('filtro_de_conteudo', 2,5, 100, 300, 300)== 'v'):
        get_image('pesquisar', 2, 50, 100, 300, 300)
        sleep(2)
    else:
        cursor.hotkey('alt', 'l')
        (aux_x, aux_y) = get_pos_image('processo', 4, 2, 50, 400, 400)
        cursor.click(aux_x, aux_y + 18)
    sleep(0.5)
    cursor.write(num_aux)
    sleep(1)
    cursor.hotkey("tab")
    sleep(0.3)
    cursor.hotkey("tab")
    sleep(0.3)
    cursor.hotkey('alt', 'c')
    sleep(1)
    cursor.hotkey('f12')
    sleep(8)



# procura imagem de pendeência na tela, finalizando se houver
def finalize_pendencias(qtd_search):
    global tem_pendencia
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/pendencias.png'):
            cursor.hotkey('F')
            print(f'encontrei e finalizei pendencia na {cont + 1} tentativa.')
            tem_pendencia = True # acho que isso deveria ser excluido porque esta sendo feito diretamente nos documentos
            break
        else:
            sleep(3)
            print(f'nao encontrei pendencia na {cont + 1} tentativa.')
            cont += 1
            if cont == int(qtd_search):
                #tem_pendencia = False
                break



# procura imagem de aviso na tela, finalizando se houver
def finalize_aviso(qtd_search):
    global tem_aviso
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/aviso.png'):
            sleep(1)
            cursor.hotkey('alt', 'o')
            sleep(1)
            print(f'finalizei aviso na {cont +1} tentativa.')
            break
        else:
            sleep(2)
            print(f'nao encontrei aviso na {cont + 1} tentativa.')
            cont += 1
            if cont == int(qtd_search):
               break


# procura imagem de aviso na tela, finalizando se houver
def finalize_confirmacao(qtd_search):
    cont = 0
    while True:
        if cursor.locateCenterOnScreen(f'assets/confirmacao.png'):
            sleep(1)
            cursor.hotkey('alt','s')
            print(f'encontrei e finalizei confirmacao na {cont + 1} tentativa.')
            break
        else:
            sleep(3)
            print(f'nao encontrei confirmacao na {cont+ 1} tentativa.')
            cont += 1
            if cont == int(qtd_search):
                break


def proch_atos_do_doc():
    img_atos = cursor.locateOnScreen('assets/atos_doc.png')
    if img_atos:
        cursor.click(img_atos)
        print('encontrei atos do documento logo de cara, na primeira tela.')

    elif img_atos is None:
        cont = 0
        img_decisao = cursor.locateOnScreen('assets/decisao.png')
        img_ato_ord = cursor.locateOnScreen('assets/ato_ord.png')
        while cont < 11:
            if img_decisao:  # se achar a decisão, clica e procura atos do documento
                cursor.click(img_decisao)
                print(f'achei a decisão na {cont + 1} vez.')
                sleep(4)
                img_atos = cursor.locateOnScreen('assets/atos_doc.png')
                if img_atos:  # se achar atos, clica e sai da função
                    cursor.click(img_atos)
                    print(f'Achei e cliquei no atos do documento da {cont + 1} decisao.')
                    sleep(1)
                    break
                else:  # se achar a decisão mas nao tiver atos, procure a proxima decisao e atos novamente
                    print(f'nao achei atos do documento na {cont + 1} decisão.')
                    img_decisao = cursor.locateOnScreen('assets/decisao.png',
                                                        region=(img_decisao[0] - 10, img_decisao[1] + 10, 200, 500))
                    cont += 1
                    if cont >= 3:
                        if img_ato_ord:  # se achar ato ordinatorio, clica e procura atos do documento
                            cursor.click(img_ato_ord)
                            print(f'achei ato ordinatório na {cont + 1} vez.')
                            sleep(4)
                            img_atos = cursor.locateOnScreen('assets/atos_doc.png')
                            if img_atos:  # se achar atos, clica e sai da função
                                cursor.click(img_atos)
                                print(f'Achei e cliquei no atos do documento do {cont + 1} ato ordinatorio.')
                                sleep(1)
                                break
                            else:
                                img_ato_ord = cursor.locateOnScreen('assets/ato_ord.png', region=(
                                    img_ato_ord[0] - 10, img_ato_ord[1] + 10, 200, 500))
                                cont += 1

                        else:
                            print(f'nao achei ato ordinatório na {cont + 1} vez. Então encerrei')
                            #break
                            exit()
                            #cont += 1

            else:  # Se nao achar decisão, procura ato ordinatorio
                print(f'Como nao achei decisão, vou procurar ato ordinatório na {cont + 1} vez.')
                if img_ato_ord:  # se achar ato ordinatorio, clica e procura atos do documento
                    cursor.click(img_ato_ord)
                    print(f'Achei ato ordinatório na {cont + 1} vez.')
                    sleep(4)
                    #cont += 1
                    img_atos = cursor.locateOnScreen('assets/atos_doc.png')
                    if img_atos:  # se achar atos, clica e sai da função
                        cursor.click(img_atos)
                        sleep(1)
                        break
                    else:  # se achar ato ordinatorio mas nao tiver atos acrescente o contador e faça comparaçoes
                        print(f'Nao achei atos do documento no {cont + 1} ato. Vou tentar incrementar o campo de busca')
                        img_ato_ord = cursor.locateOnScreen('assets/ato_ord.png', region=(
                            img_ato_ord[0] - 10, img_ato_ord[1] + 10, 200, 500))
                        cont += 1
                        if cont > 8:
                            print(f'nao achei ato ordinatorio com arvore.Contador numero {cont + 1}.')
                            break
                else:
                    #cont += 1
                    print(f'nao tem mais ato ordinatorio, entao finalizei na {cont + 1} vez.')
                    exit()



def proc_novo():
    get_image('novo',6, 2, 2)
    #função porque vamos acrescentar mais alguma coisa

def proc_requerido():
    get_image('requerido',4)

def proc_editar():
    get_image('editar',10, 2, 3)

def proc_carta():
    get_image('carta',5)

def gerar_atos():
    get_image('gerar_atos',4)

def proc_tipo_de_ato(numero_modelo):
    (aux_x, aux_y) = get_pos_image('tipo_de_ato', 2)
    cursor.click(aux_x - 20, aux_y)
    sleep(1)
    cursor.click(aux_x - 20, aux_y + 50)
    sleep(1)
    cursor.hotkey('tab')
    sleep(0.5)
    if (str(numero_modelo)=='502201'):
        cursor.write('21')
    if (str(numero_modelo) == '506136'):
        cursor.write('20')
    sleep(0.2)
    cursor.hotkey('tab')
    sleep(0.2)
    cursor.write('15')
    sleep(0.2)
    cursor.hotkey('tab')
    sleep(0.2)
    if (str(numero_modelo) == '506136'):
        cursor.hotkey('tab')
    cursor.write(numero_modelo) #comum
    #cursor.write('502201') #monitoria
    sleep(0.2)
    cursor.hotkey('tab')
    #cursor.hotkey('alt','s')

def copiar_para_outra_fila(fila):
    cursor.hotkey('f5')
    sleep(6)
    get_image('copiar_para_outra_fila',4)
    sleep(2)
    (aux_x, aux_y) = get_pos_image(fila, 3)
    if(aux_x,aux_y):
        cursor.click(aux_x - 20, aux_y)
    else:
        print(f'deveria parar aqui porque nao achei a imagem {fila}')
    sleep(1)
    cursor.hotkey('alt', 's')
    sleep(2)
    cursor.hotkey('f5')
    #aqui já estou indo para o ato ord
    sleep(5)
    get_image('aac_v', 3)
    sleep(3) # era 4 mudei para 3 nao sei se e melhor



def emitir_ato_ordinatorio(numero):
    get_image('emitir_ato_ordinatorio', 5)
    sleep(5)
    (aux_x, aux_y) = get_pos_image('modelo_ato', 5)
    if (aux_x, aux_y):
        cursor.click(aux_x + 45, aux_y + 4)
    else:
        print(f'deveria parar aqui porque nao achei a imagem do modelo do ato')
    sleep(1)
    cursor.write(str(numero))
    cursor.hotkey('tab')
    sleep(1)
    finalize_aviso(2)
    finalize_confirmacao(2)
    finalize_pendencias(2)
    sleep(6)
    cursor.hotkey('alt', 't')
    sleep(6)
    cursor.hotkey('ctrl', 'l')
    sleep(0.5)
    cursor.write('Dar')
    sleep(1)
    # precisa completar

def vista(destinatario):  #precisa melhorar futuramente
    copiar_para_outra_fila('fila_aac')
    get_image('tres_pt_azul',2)
    if destinatario == 'mp':
        get_image('vista_mp',2)
        get_image('mp', 2)
    elif destinatario == 'def':
        get_image('vista_def', 2)
        get_image('def', 2)

    sleep(3)
    finalize_aviso(2)
    finalize_confirmacao(1)
    finalize_pendencias(1)
    sleep(8)
    cursor.hotkey('alt', 'e')
    sleep(25)
    finalize_aviso(3)
    cursor.hotkey('f5')


def liberar():
    cursor.hotkey('ctrl', 'l')



def gerar_senha(num_proc, favorecido):
    usu = get_user()
    val=''
    if(exists_image('saj_aberto',1, 1,1, 50, 50)=='f'):
        if(exists_image('edge_rodape',2,300, 600, 350, 160)=='v'):
            get_image('min_browser', 2, 750, 2, 250, 100)
            #get_image('edge_rodape', 2, 300, 600, 350, 160)
        else:
            get_image('up',2,350, 680, 350, 80)
            sleep(3)
            get_image('min_browser', 2, 750, 2, 250, 100)
            get_image('edge_rodape',2,300, 600, 350, 168)
    sleep(2)
    get_image('andamento', 2, 50, 10, 200, 150)
    # VERIFICAÇÃO DE CAPSLOCK - IMPORTANTE ANTES DAS ESCRITAS
    if (get_capslock_state() == 1):
        cursor.press('capslock')
    cursor.hotkey('s')
    sleep(3)
    cursor.write(num_proc)
    sleep(1)
    #VERIFICANDO SE A SENHA É PARA PARTE
    if(favorecido == 'parte'):
        # VERIFICAMOS A VALIDADE DA SENHA
        (aux_x, aux_y) = get_pos_image('validade', 4)
        cursor.click(aux_x, aux_y + 18)
        sleep(1)
        cursor.hotkey('ctrl', 'c')
        val = clipboard.paste()
        aux = val.split('/')
        # print(aux)
        dia = aux[0]
        mes = aux[1]
        ano = aux[2]
        ano_atual = date.today().year
        ano_corrigido = ano

        if (ano_atual >= int(ano)):
            ano_corrigido = int(ano) + 2

        ano_correto = str(ano_corrigido)
        print(ano_corrigido)
        nova_data = dia + mes + ano_correto
        print(nova_data)
        cursor.write(nova_data)
    else:
        aux = favorecido
        get_image('inclui_uma_linha', 1, 300, 200, 600, 400)
        sleep(2)
        get_image('mais',1, 30, 300, 300, 300)
        sleep(1)

        (aux_x, aux_y) = get_pos_image('dow', 4, 100, 200,200,380)
        #cursor.click(aux_x, aux_y + 18)

        get_image('dow', 1, 50, 300, 300, 300)
        get_image('outros', 1, 50, 200, 250, 300)
        sleep(1)
        cursor.hotkey('tab')
        cursor.write(aux)
        sleep(1)
        foto = cursor.screenshot(region = (aux_x+18, aux_y-15, 100, 15))
        foto.save(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\foto - {favorecido}.pdf')
        cursor.hotkey('alt', 'g')



    sleep(3)
    #get_image('salvar',2, 80, 500, 300, 260)
    sleep(2)
    cursor.hotkey('alt', 'm')
    if(exists_image('aviso',2, 200, 200, 200, 200)=='v'):
        cursor.hotkey('alt', 'o')
        sleep(1)
        #cursor.hotkey('alt', 's')
        sleep(1)
        cursor.hotkey('alt', 'm')

    sleep(2)
    get_image('tic',1, 200,100, 250,250)
    sleep(1)
    cursor.hotkey('alt', 'i')
    sleep(5)
    cursor.write(f'C:\\Users\\{usu}\\OneDrive\\Documentos\\Emails\\Senha de acesso - {num_proc}.pdf')
    sleep(2)
    cursor.hotkey('enter')
    sleep(2)
    cursor.hotkey('s')
    sleep(2)
    get_image('fechar_senha', 2, 600, 100, 400, 300)

