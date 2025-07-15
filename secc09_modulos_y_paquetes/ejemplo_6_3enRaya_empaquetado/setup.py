from setuptools import setup, find_packages

setup(
    name='juego3raya',
    version='0.1',
    packages=find_packages(),  

    entry_points={
        'console_scripts': [
            'juego3raya = juego3raya.main:lanzar_vs_CPU',
        ],
    },

)

