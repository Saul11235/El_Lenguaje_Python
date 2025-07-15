from setuptools import setup, find_packages

setup(
    name='miPaquete',
    version='0.2',
    packages=find_packages(),  
    entry_points={
        'console_scripts': [
            'miComando= miPaquete.miModulo:miFuncion',
        ],
    },
)
