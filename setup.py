from setuptools import setup, find_packages

setup(
    name='opportunity',
    version='0.0.1',
    description='Simple job board.',
    author='Gamaliel Chávez',
    #author_email='',
    url='https://github.com/commoncode/opportunity',
    keywords=['django', 'job', 'board'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        # TODO
    ]
)
