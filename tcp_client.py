import socket
import argparse

class TCPTools():
    def __init__(self):
        """Gets the command-line arguments"""
        parser = argparse.ArgumentParser()
        parser.add_argument("site", help="The site you want to use GET on")
        parser.add_argument("--p", help="The port you want to use GET on", type=int)
        args = parser.parse_args()
        
        self.target_host = args.site

        if args.p:
            self.target_port = args.p
        else:
            self.target_port = 80

    def create_tcp_client(self):
        """Creates the TCP socket and connects it"""
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect the client
        client.connect((self.target_host,self.target_port))
        self.client = client

    def do_tcp_get(self):
        """Do a GET"""
        # send some data, note we have to encode for python 3
        client = self.client
        get_req = "GET / HTTP/1.1\r\nHost:"+self.target_host+"\r\n\r\n"
        
        print("GET REQUEST: \n"+get_req)

        client.send(get_req.encode('utf-8'))

        # receive some data, note we have to decode for python 3 if we want
        # to use the string somehow. It can be read (with difficulty)
        # without decoding.
        response = client.recv(4096)
        print(response.decode('utf-8'))

    def main(self):
        self.create_tcp_client()
        self.do_tcp_get()

if __name__ == '__main__':
    tcpc = TCPTools()
    tcpc.main()