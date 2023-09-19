from setuptools import setup, find_packages

setup(
    name="tickprint",
    version="0.1",
    packages=find_packages(),
    py_modules=["tickprint"],  # This is the name of your Python file
    install_requires=[
        'threading; python_version<"3.7"'  # Only for older Python versions
    ],
    author="Dion Timmer",
    author_email="diontimmer@live.nl",
    description="Prints attributes of an object every set interval",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
