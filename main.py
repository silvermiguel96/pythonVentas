
clients = 'pablo,ricardo,'

def crear_cliente(client_name):
    global clients
    clients += client_name
    _add_coma()

def list_clients():
    global clients
    print(clients)

def _add_coma():
    global clients
    clients += ','

if __name__ == '__main__':
  
  list_clients()
  crear_cliente('david')
  list_clients()