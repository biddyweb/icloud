from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='pyicloud',
    version='0.7.3',
    url='https://github.com/d3xt3-bitstechlab/pyicloud/tree/master/pyicloud',
    description=(
       
    ),
    author='Bits TechLab',
    author_email='reachus@bitstechlab.com',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'icloud = pyicloud.cmdline:main'
        ]
    },
)
