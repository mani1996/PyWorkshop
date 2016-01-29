import asyncore,socket

class clientHandler(asyncore.dispatcher):
    
    def __init__(self,socket,address,clientList,chunk_size = 256):
        asyncore.dispatcher.__init__(self,sock = socket)
        self.chunk_size = chunk_size
        self.address = address
        self.clientList = clientList
        self.socket = socket
        return 
        
    def handle_read(self):
            data = self.recv(self.chunk_size)
            if data:
                for client in self.clientList:
                    if client != self.socket:
                        client.send(data)
            
    def handle_close(self):
        print "Closing client " + str(address)
        self.close()
        
class Server(asyncore.dispatcher):
    
    def __init__(self,address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.bind(address)
        self.listen(5)
        self.clientList = []
        return 
        
    def handle_accept(self):
        client,addr = self.accept()
        print "Connected to " + str(addr)
        self.clientList.append(client)
        clientHandler(socket = client,address = addr,clientList = self.clientList)
        return 
        
    def handle_close(self):
        self.close()
        print "Closing server."

if __name__ == '__main__':
    address = ('0.0.0.0',5000)
    server = Server(address)
    try:
        print "Server listening on " + str(address) 
        asyncore.loop(0.2,use_poll = True)
    except KeyboardInterrupt:
        print "Closing server."
        server.close()
        
        