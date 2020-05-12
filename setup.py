from setuptools import setup

APP_NAME = 'SZ2pdf'

setup(
    name=APP_NAME,
    version='0.1.0',
    py_modules=['SZ2pdf'],
    url='https://github.com/SiKreuz/SZ2pdf',
    license='MIT',
    author='Simon Kreuzer',
    author_email='mail@monsi.org',
    description='This tool downloads the newest paper as pdf from the SZ using your login credentials.',

    python_requires='>=3.5',
    entry_points='''
    [console_scripts]
    SZ2pdf=SZ2pdf:cli
    ''',
    install_requires=[
        'mechanize>=0.4.5',
        'appdirs>=1.4.4',
        'click>=7.1.2'
    ]
)
