import socket
import sys

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

data = my_socket.recv(1024)
print "recieved: \n%s" % data
says = sys.stdin.readline()
print "this is says"
print says
my_socket.sendall(says)
my_socket.close()