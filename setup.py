from setuptools import setup


def get_readme():
    with open('README.rst', 'r') as fd:
        return fd.read()


setup(
    name='frozen_box',
    version=__import__('frozen_box').__version__,
    description='Store Python objects in a immutable manner and provide fast attribute lookup',
    long_description=get_readme(),
    long_description_content_type='text/x-rst',
    author='Leavers',
    author_email='leavers930@gmail.com',
    url='https://github.com/leavers/frozen',
    py_modules=["frozen_box"],
    packages=['frozen_box'],
    python_requires=">=3.6",
    install_requires=[],
    tests_require=[
        'pytest',
    ],
    extras_require={},
    platforms='any',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
