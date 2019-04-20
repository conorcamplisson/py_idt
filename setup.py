import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_idt",
    version="0.0.1",
    author="Conor Camplisson",
    author_email="conor.camplisson@gmail.com",
    description="A python interface for creating IDT bulk oligo order forms in Excel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/conorcamplisson/py_idt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas',
        'xlsxwriter',
        'xlrd'
    ],
)

