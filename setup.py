import setuptools

setuptools.setup(
    name="PyScramble",
    version="0.1.0",
    author="Mike Matera",
    author_email="matera@lifealgorithmic.com",
    description="Scramble an executable Python script.",
    url="http://www.lifealgorithmic.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],

    install_requires=[
    ],

    packages=[
        'pyscramble',
    ],
    
    scripts=[
        'pyscramble/pyscramble', 
    ],
)
