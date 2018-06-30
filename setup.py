import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ColourList",
    version="1.0",
    author="Gauransh Mathur",
    author_email="gauranshmathur1999@gmail.com",
    description="A colour module made for web design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GauranshMathur/ColourList",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)