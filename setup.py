from setuptools import setup, find_packages


setup(
    name='report-classic-project',
    version='0.1',
    license='MIT',
    author="Cãmara Municipal de São Bernardo do Campo, SP, Brazil",
    author_email='informatica@camarasbc.sp.gov.br',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/cmsbc/report-classic-project',
    keywords='ReportClassic Project',
    install_requires=[
          'reportlab',
          'django',
          'datetime'
      ],

)
