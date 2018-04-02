import threading

def hello_world():
    threading.Timer(60.0, hello_world).start() # called every minute
    print("Hello, World!")

hello_world()
