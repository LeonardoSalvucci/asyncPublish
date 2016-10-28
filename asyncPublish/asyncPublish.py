from time import sleep

import pika

class asyncPublish:

    def __init__(self, host='localhost', port=5672, usr='guest', password='guest', vHost='/'):
        self.host = host
        self.port = port
        self.usr = usr
        self.password = password
        self.vHost = vHost

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
                    if queue.__class__ == str:
                        channel.queue_declare(
                            queue=queue,
                            durable=True,
                        )
                        channel.queue_bind(exchange=exchange, queue=queue, routing_key='')
                    elif queue.__class__ == dict:
                        channel.queue_declare(
                            queue=queue['name'],
                            durable=True,
                            arguments=queue['arguments'],
                        )
                        channel.queue_bind(exchange=exchange, queue=queue['name'], routing_key='')

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