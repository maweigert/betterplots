from setuptools import setup, find_packages
#------------------------------------------------------------------------------------

setup(
    name='betterplots',
    version='0.1.0',
    description='better plots',
    long_description_content_type='text/markdown',
    author='Martin Weigert',
    author_email='martin.weigert@epfl.ch',
    license='BSD 3-Clause License',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    install_requires=[
        'numpy',
        'seaborn>=0.13.0',
    ],
    package_data={"betterplots":['fonts/*']},
)
