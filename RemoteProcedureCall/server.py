from xmlrpc import server
from xmlrpc.server import SimpleXMLRPCServer


class Operations:
    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b


with SimpleXMLRPCServer(("localhost", 6789)) as server:
    server.register_instance(Operations())
    print("Serving XML-RPC on localhost")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Exiting...")
        SystemExit()
