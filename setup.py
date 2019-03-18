import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
requirements=['requests','PySocks','bs4','paramiko','pexpect','mysql-connector','scapy','stem']

setuptools.setup(
    name="bane",
    version="1.4.8",
    author="AlaBouali",
    author_email="trap.leader.123@gmail.com",
    description="cyber security library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/bane",
    py_modules=["bane", "payloads"],
    install_requires=requirements,
    python_requires=">=2.7",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License ",
        "Operating System :: Unix",
    ],
)
