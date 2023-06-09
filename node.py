import logging

from node_socket import UdpSocket

class Node:

    def __init__(self, my_id: int, my_port: int):
        self.my_id = my_id
        self.my_port = my_port
        self.node_socket = UdpSocket(my_port)

    def start(self):
        pass

    def listen_procedure(self) -> str:
        inbound_message, address = self.node_socket.listen()
        return inbound_message

    def sending_procedure(self, message, port):
        self.node_socket.send(message, port)