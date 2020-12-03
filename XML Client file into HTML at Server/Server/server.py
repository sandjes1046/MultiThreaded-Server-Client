
import socket
#add threading support
import threading # supported in python 3 and above
from xml_to_html_generator import xml_to_html_transform######


''' the threading class ...has 1- the run function and 2- the thread as prent .....'''
class ClientConnectionThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        print(f'starting up client connection from: {self.clientAddress}')

        
    # the run function for the thread
    def run(self):
        print ("Connection from : ", self.clientAddress)
#        file_name = 'file1.txt'+str(self.connection_number)
        
        # get filename and size
        metadata_line_raw = self.csocket.recv(1024)
        metadata_line= metadata_line_raw.decode()
        info=metadata_line.splitlines()[0]
        file_name = info.split()[0]
        #file_name = file_name + info.split()[1]
        amount_expected = int(info.split()[1])
        name = file_name.split(".")####
        new_filename =name[0]
        new_filename = new_filename + ".html"
        
        amount_received = 0
        print (f"File name is {file_name} with size of {amount_expected}")    
        
        f = open(file_name,"wb")
        while amount_received < amount_expected:   
            data = self.csocket.recv(4096)
            if not data:
                break
            amount_received += len(data)
            f.write(data)
        f.close()
        # Let the client know the file was received
        msg = 'The file ' + file_name + ' was received correctly'
        self.csocket.sendall(msg.encode())
        self.csocket.close()
        print ("Client at ", self.clientAddress, " disconnected...")
        xml_to_html_transform(file_name,"student_advising.xslt",new_filename)

# Create a TCP/IP socket
# Server Main
# Bind the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} at port {server_address[1]}')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
connection_number=1
# Listen for incoming connections
while True:
    # Wait for a connection
    sock.listen(1)
    print('waiting for a connection')
    clientsock, clientAddress = sock.accept()
    connection_number +=1
    try:
        print('connection from', clientAddress)
        new_connection_thread = ClientConnectionThread(clientAddress, clientsock)
        new_connection_thread.start()
    except:
        print('Server Error...')


