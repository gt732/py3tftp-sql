from setuptools import setup


try:
    import pypandoc
except ImportError:
    pypandoc = None


def readme():
    with open("README.md", "r") as f:
        readme_md = f.read()
        return readme_md


setup(
    name="py3tftpsql",
    version="1.0.1",
    description="Python 3 asynchronous TFTP server.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/gt732/py3tftp-sql",
    author="Matt O.",
    author_email="matt@mattscodecave.com",
    license="MIT",
    keywords="async asynchronous tftp",
    packages=["py3tftpsql"],
    include_package_data=True,
    entry_points={"console_scripts": ["py3tftpsql = py3tftpsql.__main__:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
    ],
)
