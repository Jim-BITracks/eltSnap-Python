import setuptools
import pkg_resources
import pathlib


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name='eltsnap',
    url='https://github.com/Jim-BITracks/eltSnap-Python.git',
    author='Jim Miller',
    version='0.0.1',
    license='MIT license',
    description='Third version test',
    packages=['eltsnap'],
    package_dir={'eltsnap': 'eltsnap'},
    package_data={'eltsnap': ['html/*', 'html/bootstrap-4.3.1-dist/css/*',
                                           'html/bootstrap-4.3.1-dist/js/*',
                                           'html/images/*'], },
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
