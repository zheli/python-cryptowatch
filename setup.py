"""Package setup file."""
import os

use_helper = False

try:
    from pip.req import parse_requirements
except ModuleNotFoundError: # for pip >=10
    use_helper = True

from setuptools import find_packages, setup

def parse_requirements_shim(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

def get_version():
    """Return the current version."""
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(curr_dir, 'version.txt')) as version_file:
        return version_file.read().strip()


def get_requirements(file):
    """Return a list of requirements from a file."""
    requirements = parse_requirements_shim(file) if use_helper else parse_requirements(file, session=False)
    return [str(ir.req) for ir in requirements if not None]


setup(
    name='cryptowatch',
    version=get_version(),
    description='Unofficial wrapper for for the Cryptowatch public Data API.',
    author='uoshvis',
    url='https://github.com/uoshvis/python-cryptowatch',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    setup_requires=[
        'pytest-runner',
        'pytest-pylint'
        ],
    tests_require=get_requirements('requirements_test.txt'),
    platforms='any'
)
