import pika
from common.system import readconfig
from common.crypt import AESCipher
from common.logger import GetFileLogger

class broker:

    def __init__(self):
        self.connected = False
        self.log = GetFileLogger()
        try:
            self.handle = self.connect()
            self.channel = self.handle.channel()
            self.connected = True
            self.log.info("Connected to broker")
        except Exception as e:
            self.log.info("Failed to connect to broker:" + e)

    def connect(self):
        crypt = AESCipher()
        config = readconfig('message_bus.json')
        credentials = pika.PlainCredentials(config['user'], crypt.decrypt(config['password']))
        parameters = pika.ConnectionParameters(
            config['host'],
            config['port'],
            config['vhost'],
            credentials
        )
        return pika.BlockingConnection(parameters)

    def close(self):
        self.handle.close()

    def send_message(self, dest, message):
        self.channel.queue_declare(queue=dest)
        self.channel.basic_publish(exchange='', routing_key=dest, body=message)
        self.log.debug("Message sent to " + dest)

    def fecth_message(self, source):
        self.channel.queue_declare(queue=source)
        method_frame, header_frame,body = self.channel.basic_get(queue=source)
        if method_frame is None:
            self.log.debug("Got empty message")
            return ''
        else:
            self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            self.log.debug("Got loadeded message")
            return body.decode('utf-8')