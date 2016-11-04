# asyncPublish

class asyncPublish:
    asyncPublish(_host_=**'localhost'**, _port_=**5672**, _usr_=_'guest'_, _password_=**'guest'**, _vHost_=**'/'**)
    
    
    def publish(message, exchange, queues)
        message (string)
        exchange (string)
        queues (list)
        
            queue (list of strings for one or multiple queues)
            queue (dict -> {'name':'queueName',
                            'arguments': {
                                'x-message-ttl':	        3000,
                                'x-dead-letter-exchange':	'Prueba',
                             }
                           }
            queue (both list of strings and dict)
