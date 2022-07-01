ReportClassic Project
===============
This is a ReportClassic Project made to print labels and reports in PDF.

Installing
============

.. code-block:: bash

    pip install report-classic-project

Usage
=====

.. code-block:: python

    from utils.general.report_line_detail import ReportLineDetail
    from utils.general.report_mline_detail import ReportMLineDetail

    def sample_line_detail(request):
    relat = ReportLineDetail(titulo="Câmara Municipal de de São Bernardo do Campo",  # noqa: E501
                                subtitulo="SAG", pag_rodape=True,
                                data_rodape=True, texto_rodape="Texto Rodapé",  # noqa: E501
                                filename='tutorial.pdf', pagesize='A4')
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
