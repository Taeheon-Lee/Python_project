from setuptools import setup, find_packages

setup(
    name             = 'ai42',
    version          = '1.0.0',
    description      = 'Package about loading.py and logger.py',
    author           = 'tlee(Taeheon Lee)',
    author_email     = 'tlee@student.42.us.org',
    url              = 'https://github.com/Taeheon-Lee/Python_bootcamp/tree/master/day02/ex04',
    download_url     = 'https://github.com/Taeheon-Lee/Python_bootcamp/blob/master/day02/ex04/ai42-1.0.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(),
    keywords         = ['python_bootcamp', 'ai42'],
    python_requires  = '>=3.7',
    package_data     =  { },
    zip_safe=False,
    classifiers      = ['Programming Language :: Python :: 3.7']
)
