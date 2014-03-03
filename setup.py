from setuptools import setup, find_packages

setup(
    name='django-linkage',
    version='0.1.dev',
    description='Simple Links and Menus for Django',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='http://github.com/funkybob/django-linkage',
    keywords=['django',],
    packages = find_packages(exclude=('tests*',)),
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    requires = [
        'Django (>=1.6)',
        'django-polymorphic (>=0.5.1)',
    ],
)
