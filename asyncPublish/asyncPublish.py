from time import sleep

import pika

class asyncPublish:

    def __init__(self, host=None, port=None, usr=None, password=None, vHost=None):

        if host:
            self.host = host
        else:
            self.host = 'localhost'

        if port:
            self.port = port
        else:
            self.port = 5672

        if usr:
            self.usr = usr
        else:
            self.usr = 'administrador'

        if password:
            self.password = password
        else:
            self.password = 'sr650'

        if vHost:
            self.vHost = vHost
        else:
            self.vHost = ''

    def publish(self, message, exchange, queues):
        i=0
        while i<10:

            try:
                connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(
                            host=self.host,
                            port=self.port,
                            virtual_host=self.vHost,
                            credentials=pika.PlainCredentials(
                                    username=self.usr,
                                    password=self.password)
                            ))

                # Open the channel
                channel = connection.channel()

                channel.exchange_declare(
                    exchange=exchange,
                    exchange_type='fanout',
                    durable=True,
                )

                for queue in queues:
                    channel.queue_declare(
                        queue=queue,
                        durable=True,
                    )
                    channel.queue_bind(exchange=exchange,queue=queue)

                # Turn on delivery confirmations
                channel.confirm_delivery()

                # Send a message
                msj= channel.basic_publish(exchange=exchange,
                                         routing_key='',
                                         body=message,
                                         properties=pika.BasicProperties(content_type='text/plain',
                                                                         delivery_mode=2))

                channel.close()
                connection.close()
                return msj

            except:
                pass
            i+=1
            sleep(0.5)
        return False