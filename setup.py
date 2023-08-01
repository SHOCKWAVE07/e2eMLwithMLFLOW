import setuptools
with open("README.md", 'r',encoding='utf-8') as f:
    long_description=f.read()

__version__ = "0.0.0"

REPO_NAME = "e2eMLwithMLFLOW"
AUTHOR_USER_NAME = 'SHOCKWAVE07'
SRC_REPO = "e2emlProject"
AUTHOR_EMAIL = "varunraskar22@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdonw",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)