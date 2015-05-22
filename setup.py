from setuptools import setup, find_packages


setup(
    name = "aionsq",
    version = "0.0.1",
    author = "Chris Goller",
    author_email = "goller@gmail.com",
    description = ("asyncio (PEP 3156) nsq (message queue) client."),
    packages=find_packages(),
    install_requires=[
        "python-snappy==0.5", 
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe=True
)
