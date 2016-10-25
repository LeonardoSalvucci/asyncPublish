from distutils.core import setup

setup(
    name='asyncPublish',
    version='1.1.0',
    packages=['asyncPublish'],
    url='',
    license='',
    author='Leonardo Salvucci',
    author_email='le.salvucci@gmail.com',
    description='RabbitMQ async publish with confirmation',
    install_requires = [
        'pika',
    ]
)
