from setuptools import setup

APP_NAME = 'SZ2pdf'

setup(
    name=APP_NAME,
    version='0.2.0',
    py_modules=['FR2pdf', 'conf_utils', 'output_utils'],
    url='https://github.com/xorbital/FR2pdf',
    license='MIT',
    author='xorbital',
    description='This tool downloads the current newspaper as pdf from the "Sueddeutsche Zeitung" using your login '
                'credentials.',

    python_requires='>=3.5',
    entry_points='''
    [console_scripts]
    FR2pdf=FR2pdf:cli
    ''',
    install_requires=[
        'mechanize~=0.4.5',
        'appdirs~=1.4.4',
        'click~=7.1.2'
    ]
)
