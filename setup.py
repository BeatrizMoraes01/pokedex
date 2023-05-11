from cx_Freeze import setup, Executable

setup(name='Pokedex',
      version='0.1',
      description='Projeto Pokedex com Python',
      executables=[Executable('Pokedex_Python.py')])
