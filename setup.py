import os
from setuptools import find_packages, setup

setup(
    name="countdown",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="countdown in cmd",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['countdown = countdowntime:main',],
    },
    install_requires=["pywin32 >= 1.0;platform_system=='Windows'"],

)
