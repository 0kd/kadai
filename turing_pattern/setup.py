from setuptools import setup, find_packages

setup(
    name='turing_pattern',
    version="0.1.1",
    description="simulator of turing-pattern \n See https://github.com/tsuchiura/kadai for usage",
    long_description="simply simulate and visualize turing pattern, inspired by the TV show Magaten",
    url='https://github.com/tsuchiura/kadai',
    author='kudo',
    author_email='tsuchiurax@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    keywords='turing',
    install_requires=["matplotlib", "numpy"],
    )
