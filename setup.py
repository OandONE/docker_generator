from setuptools import setup, find_packages

setup(
    name="docker_generator",
    version="1.0.0",
    author="seyyed mohamad hosein moosavi raja(01)",
    author_email="mohamadhosein159159@gmail.com",
    description="This Library is for generator docker text easyer !",
    long_description=open("README.md",encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OandONE/docker_generator",
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[],
    license="MIT"
)
