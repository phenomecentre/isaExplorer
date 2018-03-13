from setuptools import setup

setup(name='isaExplorer',
      version='0.1',
      description='Explore and manipulate the Contents of ISATAB files',
      url='http://github.com/phenomecentre/isaexplorer',
      author='Noureddin Sadawi',
      author_email='n.sadawi@gmail.com',
      license='MIT',
      packages=['isaExplorer'],
      install_requires=[
          'isatools'
      ],
      zip_safe=False)
