import datetime
import os
import time

from django.conf import settings
from utils.general.report_label import ReportLabel
from utils.general.report_line_detail import ReportLineDetail
from utils.general.report_mline_detail import ReportMLineDetail


def check_media_path():
    caminho = str(settings.MEDIA_ROOT)
    if not os.path.isdir(caminho + '/tmp'):
        os.mkdir(caminho + '/tmp')
    if not os.path.isdir(caminho + '/tmp/reports'):
        os.mkdir(caminho + '/tmp/reports')
    return caminho + '/tmp/reports'


def limpa_texto(campo):
    if campo is None:
        return " "
    return campo.strip()


def limpa_diretorio():
    hora = time.time()
    diret = check_media_path()
    files = [os.path.join(diret, filename)
             for filename in os.listdir(diret)]
    for filename in files:
        if (hora - os.stat(filename).st_mtime) > 60:
            os.remove(filename)


def define_filename():
    data = datetime.datetime.now()
    diret = check_media_path()
    nome = data.strftime('%Y%m%d%H%M%S%f')
    filename = diret + '/' + nome + '.pdf'
    return filename


class ReportMethodsClass:

    def sample_label(request):
        fmt_label = {1: {0: 'Nome', 50: 'Sobrenome', 90: 'Status'},
                     2: {0: 'Nome 2', 60: 'Sobrenome 2', 80: 'Status 2'}, }

        relat = ReportLabel(filename="tutorial.pdf", pagesize='Letter')
        relat.def_label(qtde_eti_linha=2, qtde_eti_coluna=7,
                        marg_esquerda=4, marg_direita=4, marg_superior=21,  # noqa: E501
                        larg_etiqueta=101.6, tam_linha=5,
                        altura_etiqueta=33.9, esp_entre_etiqueta=6,
                        fmt_label=fmt_label)
        for i in range(1, 17):
            detalhe = ['Nome de Teste' * 10,
                       'S o b r e n o m e d e T e s t e' * 5,
                       'Status de Teste' * 5,
                       '2 Nome de Teste' * 10,
                       '2 S o b r e n o m e d e T e s t e' * 5,
                       '2 Status de Teste' * 5]
            options = {1: {'bold': True},
                       2: {'bold': True}}  # noqa: E501
            relat.label_detail(detalhe=detalhe, options=options)
        relat.render()

    def sample_mline_detail(request):
        filename = define_filename()
        relat = ReportMLineDetail(titulo="Câmara Municipal de de São Bernardo do Campo",  # noqa: E501
                                  subtitulo="SAG", pag_rodape=True,
                                  data_rodape=True, texto_rodape="Texto Rodapé",  # noqa: E501
                                  filename=filename, pagesize='A4')
        cabec = {1: {12: 'Nome', 60: 'Sobrenome', 120: 'Status'},
                 2: {12: 'Nome 2', 60: 'Sobrenome 2', 120: 'Status 2'}, }
        relat.def_mline_detail(cabec=cabec, imp_cabec=True, text_cabec="teste")
        for i in range(1, 74):
            detalhe = ['Nome de Teste' * 10,
                       'S o b r e n o m e d e T e s t e' * 5,
                       'Status de Teste' * 5,
                       '2 Nome de Teste' * 10,
                       '2 S o b r e n o m e d e T e s t e' * 5,
                       '2 Status de Teste' * 5]
            options = {1: {'bold': True},
                       2: {'bold': True, 'fontname': 'Times', 'italic': True, 'fontsize': 6}}  # noqa: E501
            relat.mline_detail(detalhe=detalhe, options=options)
        relat.render()
        arquivo = settings.MEDIA_URL + 'tmp/reports/' + filename.split("/")[-1]
        return arquivo

    def sample_line_detail(request):
        filename = define_filename()
        relat = ReportLineDetail(titulo="Câmara Municipal de de São Bernardo do Campo",  # noqa: E501
                                 subtitulo="SAG", pag_rodape=True,
                                 data_rodape=True, texto_rodape="Texto Rodapé",  # noqa: E501
                                 filename=filename, pagesize='A4')
        cabec = {12: 'Nome', 60: 'Sobrenome', 120: 'Status'}
        relat.def_line_detail(cabec=cabec)
        for i in range(1, 74):
            detalhe = ['Nome de Teste' * 10,
                       'S o b r e n o m e d e T e s t e' * 5,
                       'Status de Teste' * 5]
            options = {1: {'bold': True},
                       2: {'bold': True, 'fontname': 'Times', 'italic': True, 'fontsize': 6}}  # noqa: E501
            relat.line_detail(detalhe=detalhe, options=options)
        relat.render()
        arquivo = settings.MEDIA_URL + 'tmp/reports/' + filename.split("/")[-1]
        return arquivo
