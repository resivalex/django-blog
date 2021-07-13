import setuptools


setuptools.setup(
    name='django-blog',
    version='0.0.1',
    author='Ivan Reshetnikov',
    author_email='resivalex@gmail.com',
    description='A blog on Django',
    long_description='A blog on Django',
    long_description_content_type='text/plain',
    url='https://github.com/resivalex/django-blog',
    packages=setuptools.find_packages('.'),
    package_dir={'': ''},
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: MIT',
        'Operating System :: Linux',
    ],
    python_requires='>=3.8',
)
