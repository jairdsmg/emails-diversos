import diversos

#para=''
#assunto=''
#conteudo=''
saudacao='Prezado(a) Senhor(a)!'

def get_email(codigo):
    if(codigo==1):
        #para='cartorioriitaqua@terra.com.br'
        para = 'cartorioriitaqua@terra.com.br'
        assunto='Solicitação de Parecer - Autos: '
        conteudo='Com meus cumprimentos, encaminho a Vossa Senhoria, senha de acesso aos autos \n acima mencionados, solicitando parecer conforme Decisão de fls. '
        qtd_anexos=0
    elif (codigo == 2):
        para = 'unidade_mogicruzes@defensoria.sp.def.br'
        assunto = 'Encaminhamento de Ofício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de ofício expedido nos autos acima \n mencionados, solicitando as devidas providências.'
        qtd_anexos = 0
    elif (codigo == 2):
        para = 'unidade_mogicruzes@defensoria.sp.def.br'
        assunto = 'Encaminhamento de Ofício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de ofício expedido nos autos acima \n mencionados, solicitando as devidas providências.'
        qtd_anexos = 0
    elif (codigo == 3):
        para = 'itaquaquecetubaggg'
        assunto = 'Carta Precatória para distribuição via Malote Digital - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de carta precatória expedida \n nos autos acima  mencionados(nosso), para envio/distribuição junto à Comarca de '
        qtd_anexos = 0
    elif (codigo == 4):
        para = 'itaquaquecetubacp'
        assunto = 'Devolução de Carta Precatória via malote digital - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópias das peças produzidas nos autos de \n nº XXXXXXXXX(nosso),  para devolução via  Malote Digital à 2ª Vara Cível de Paranavaí -PROJUDI - TJPR -\n Referente ao processo de  origem nº XXXXXXXXX'
        qtd_anexos = 0
    elif (codigo == 5):
        para = 'elabgexgru'
        assunto = 'Implantação de Benefício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópias da petição inicial, Sentença, Acórdão \n e Decisão(ões) proferidas nos autos acima mencionados, para implantação do\n benefício concedido aos autor, Sr(a). XXXXX, RG XXXX, CPF XXXX. \nSolicitamos, ainda, a comunicação com este juízo quando cumprida \na referida determinação anexa.'
        qtd_anexos = 0
    elif (codigo == 6):
        para = 'jairdsmg@gmail.com'
        assunto = 'Intimação de Nomeação - Autos: '
        conteudo = 'Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que manifeste se aceita o encargo, ciente de que os honorários periciais serão suportados exclusivamente pela Defensoria Pública conforme Decisão de fls. '
        qtd_anexos = 0
    elif (codigo == 7):
        para = 'jairdsmg@gmail.com'
        assunto = 'Intimação de Nomeação - Autos: '
        conteudo = 'Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que estime seus honorários nos termos da Decisão de fls. '
        qtd_anexos = 0
    elif (codigo == 8):
        para = 'jairdsmg@gmail.com'
        assunto = 'Cientificação  - Expedição de MLE - Autos: '
        conteudo = 'Com meus cumprimentos, cientifico Vossa Senhoria de que houve a expedição de MLE em seu favor, referente aos autos acima mencionados, não havendo necessidade de comparecimento em cartório, uma vez que os valores foram/serão depositados na conta informada no processo. '
        qtd_anexos = 0
    elif (codigo == 9):
        para = 'perito@gmail.com'
        assunto = 'Intimação- Autos: '
        conteudo = 'Com meus cumprimentos, intimo Vossa Senhora acerca da reserva de honorários \n efetuada junto à DPESP, para que inicie seus trabalhos referentes aos autos acima \n mencionados.'
        qtd_anexos = 0

    return(para,assunto,conteudo,qtd_anexos)