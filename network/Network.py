
from SecureP2PNetwork import SecureNode

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance

class Network(SecureNode, SingletonClass):
    def __init__(self, host, port):
        super(SecureNode, self).__init__(host, port, None)
    def startNode(self):
        self.send


    #def generateRSAKey(self):


