from setuptools import setup, find_packages

setup(
    name='mcq_generator',
    version='0.0.1',
    author="Paul Ntalo",
    author_email="ntalops@yahoo.com",
    install_requires=["openapi", "langchain", "streamlit","python-dotenv", PyPDF2],
    packages=find_packages(),
)


