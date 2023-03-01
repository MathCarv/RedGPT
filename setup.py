from distutils.core import setup
setup(
  name = 'RedGPT',
  packages = ['RedGPT'],
  version = '0.1.6',
  license='GPLv3',
  description = 'A penetration testing findings generator using ChatGPT.',
  author = 'Matheus Carvalho',
  author_email = 'matheus.camara@gec.inatel.br',
  url = 'https://github.com/MathCarv/RedGPT',
  keywords = ['ChatGPT', 'Pentesting', 'Penetration Testing', 'Findings Generator'],
  install_requires=[
    'revChatGPT'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
  ],
)
