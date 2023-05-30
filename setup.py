from setuptools import setup
setup(
    name='LNP.PYAPP',
    version='0.0.1',
    packages=['src'],
    install_requires=[
        'requests',
        'importlib; python_version == "3.11"',
    ],
)