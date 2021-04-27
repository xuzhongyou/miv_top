import sys
from setuptools import setup,find_packages
import top

setup(
    name = 'mivtop',
    version = top.__version__,
    author = top.__author__,
    packages = find_packages(include=['top','top.*']),
    entry_points = {
        'console_scripts':[
            'mivtop=top.mivtop:main'
        ]\
    },
    install_requires=([
        'nvidia-ml-py==11.*',
        'psutil',
        'pyyaml',
        'pymysql',
        'tabulate'
    ])
)