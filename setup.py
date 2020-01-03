from setuptools import setup, find_packages

## Gets content of README.rst for SetupTools 'readme' value
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name="hr",
    version="0.1.0",
    description="Adds/Updates user accounts on servers",
    long_description=readme,
    author="Shawn OG",
    author_email="49504334+MacOG@users.noreply.github.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
