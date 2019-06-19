# 나만의 외부모듈 만들기
from setuptools import setup

setup(
    name="bhyutils",
    version="0.0.1",
    description="util modules by Hayeon",
    url="http://github.com/bhy304/bhyutils",
    author="Hayeon Baek",
    author_email="bhy0512@gmail.com",
    license="MIT",
    packages=['bhyutils'],
    intall_requires=['requests'],
    zip_safe=False
)

# 설치 : pip install -e .
# https://pypi.org/
# 만인의 외부모듈 만들기 : python setup.py register sdist upload 