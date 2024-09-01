from setuptools import setup, find_packages 

setup(
    name='khwarizm',
    version='0.0.1',
    packages=find_packages(include=['khwarizm', 'khwarizm.*'],exclude=['tests']),
    py_modules=[None],
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'keras',
        'pytorch',
    ],
    author='Ahmed Alghali',
    author_email='ahmed@offsechq.com',
    description='khwarizm is a machine learning library that boosts your productivity and provides you with insights from your data.',
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)