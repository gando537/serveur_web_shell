#!/usr/bin/python3
import os, select, socket, sys, signal

class Server :

	def __init__(self, port) :
		self.host = '127.0.0.1'
		self.port = port
		self.MAXBYTES = 10000
		self.sockets_list = []
		self.nb_client = 0
		self.exception_sockets = []
		self.serversocket = 0

	def _connexion_(self) :
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.bind((self.host, self.port))
		self.serversocket.listen()
		self.sockets_list = [self.serversocket,sys.stdin]

	def _get_host(self):
		return self.host

	def _get_port(self):
		return self.port

	def _get_nb_client(self):
		return self.nb_client

	def _get_socket(self):
		return self.serversocket

	def _set_nb_client(self):
		self.nb_client += 1

	def _selected(self):
		self.read_sockets, _, self.exception_sockets = select.select(self.sockets_list, [], self.sockets_list)

def capter_INT(sig_num, frame):
	for pid in proces:
		os.kill(pid, signal.SIGINT)
	signal.alarm(1)

def capter_ALRM(sig_num, frame):
	print("\n[serveur] SIGINT reçu, ferméture des connections...")
	print("Bye!!!")
	server.serversocket.close()
	sys.exit(0)

def main(server):
	server._selected()
	sock = server._get_socket()
	while True :
		client_socket, client_address = sock.accept()
		server._set_nb_client()
		fd = client_socket.fileno()
		pid = os.fork()
		if pid == 0 :
			print("\n[serveur] nouvelle connection acceptée (pid={}, port client={})".format(os.getpid(),client_address[1]))
			proces.append(os.getpid())
			os.dup2(fd, 0)
			os.dup2(fd, 1)
			data = os.read(fd, 100000)
			os.write(2, data)
			traitant = sys.argv[1:-1]
			os.execvp(sys.argv[1], traitant)
		else:
			os.waitpid(pid, 0)
		if server.nb_client == 4:
			os.wait()

proces = []
server = Server(int(sys.argv[2]))

if __name__ == '__main__':
	signal.signal(signal.SIGINT,capter_INT)
	signal.signal(signal.SIGALRM,capter_ALRM)
	server._connexion_()
	print("""
	 @@@@@@   @@@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@  @@@  @@@@@@@
	@@@@@@@   @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@  @@@  @@@@@@@@
	!@@       @@!       @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  @@@
	!@!       !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!  @!@
	!!@@!!    @!!!:!    @!@!!@!   @!@  !@!  @!!!:!    @!@  !@!  @!@!!@!
	 !!@!!!   !!!!!:    !!@!@!    !@!  !!!  !!!!!:    !@!  !!!  !!@!@!
	     !:!  !!:       !!: :!!   :!:  !!:  !!:       !!:  !!!  !!: :!!
	    !:!   :!:       :!:  !:!   ::!!:!   :!:       :!:  !:!  :!:  !:!
	:::: ::    :: ::::  ::   :::    ::::     :: ::::  ::::: ::  ::   :::
	:: : :    : :: ::    :   : :     :      : :: ::    : :  :    :   : :
    """)
	print("[server] {} écoute sur le port {}".format(server._get_host(), server._get_port()))
	main(server)