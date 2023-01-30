import time

from SecureP2PNetwork import SecureNode

class SingletonClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Network(SecureNode):
    __metaclass__ = SingletonClass

    def __init__(self, host, port):
        super(SecureNode, self).__init__(host, port, None)
        self.host = host
        self.port = port
        self.rsa_key_pair = ""
        self.key_file = "network_test/secure_node.dat"

    def startNode(self):
        self.generateRSAKey()
    def generateRSAKey(self):
        key_file_exists = False
        try:
            with open(self.key_file, encoding="utf8") as f:
                key_file_exists = True

        except FileNotFoundError:
            None

        except IOError:
            print("File " + self.key_file + " not accessible.")
            exit

        if key_file_exists:
            SecureNode.key_pair_load(self,self.key_file, input("What is your password to unlock the node:").encode('utf8'))
        else:
            print("New node, generating a public/private identity, can take a couple of minutes...")
            SecureNode.key_pair_generate(self)
            print("New key generated!")
            password1 = input("Type your password:")
            password2 = input("Retype your password:")
            if (password1 == password2):
                SecureNode.key_pair_save(self,self.key_file, password1)
            else:
                print("Password do not match!")
                print("Try again!")
                self.generateRSAKey()

    def start(self):
        SecureNode.start(self)
        SecureNode.debug = False
        time.sleep(1)

        running = True
        while running:
            print("Commands: message, ping, discovery, status, connect, debug, stop")
            s = input("Please type a command:")

            if s == "stop":
                running = False

            elif s == "message":
                SecureNode.send_message(self,input("Message to send:"))

            elif s == "ping":
                SecureNode.send_ping(self)

            elif s == "discovery":
                SecureNode.send_discovery(self)

            elif s == "status":
                SecureNode.print_connections(self)

            elif s == "debug":
                SecureNode.node.debug = not SecureNode.debug

            elif (s == "connect"):
                host = input("host: ")
                port = int(input("port: "))
                SecureNode.connect_with_node(self,host, port)

            else:
                print("Command not understood '" + s + "'")

        SecureNode.stop(self)


network = Network("127.0.0.1", 10002)
network.startNode()
network.start();

