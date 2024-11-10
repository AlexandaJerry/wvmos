from setuptools import setup, find_packages


# Package meta-data.
NAME = 'wvmos'
DESCRIPTION = 'This package is written for MOS score prediction based on fine-tuned wav2vec2.0 model'
URL = 'https://github.com/AndreevP/wvmos'
EMAIL = 'andreev.pk@phystech.edu'
AUTHOR = 'Pavel Andreev'
REQUIRES_PYTHON = '>=3.8.10'
VERSION = '1.0'

setup(
    name="wvmos",
    version="1.0",
    packages=find_packages(),
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'librosa',
        'torch',
        'transformers'
    ],
    include_package_data=True
)
