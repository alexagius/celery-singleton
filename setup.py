from setuptools import setup,find_packages

setup(
    name='celery-singleton',
    version='0.1.2',
    description='Prevent duplicate celery tasks',
    author='Steinthor Palsson',
    author_email='steini90@gmail.com',
    url='https://github.com/steinitzu/celery-singleton',
    license='MIT',
    install_requires=[
        'celery>=4.0.0',
        'redis>=2.10.5'
    ],
    packages=find_packages()
)
