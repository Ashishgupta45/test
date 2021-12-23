from setuptools import setup
setup (name="package_twtr",
version="0.1",
description="This package contains cleaning text, stemming and removing stopwords using different funtion",
author="AshishGupta",
packages=["package_twtr"],
install_requiers= ['SnowballStemmer','numpy', 'pandas', 'stopwords', 'nltk']
)