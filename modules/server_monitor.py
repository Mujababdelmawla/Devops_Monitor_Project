from datetime import datetime

class Server:
    def __init__(self, name, ip_address, status):
        self.name = name 
        self.ip_address = ip_address
        self.status = status 

    def start(self):
        self.status = "ONLINE"
        return f"{self.name} server with {self.ip_address}  ip address is ONLINE"

    def stop(self):
        self.status = "OFFLINE"
        return f"{self.name} server with {self.ip_address} ip address is OFFLINE"

    def get_status(self):
        return f"{self.name} server with {self.ip_address} ip address current status is {self.status}"

    def to_dict(self):
        # this function is converting the data to dictionary so that we use it later for our project report
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "status": self.status,
            "checked_at": datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        }


class WebServer(Server):
    def __init__(self, name, ip_address, status, port):
        super().__init__(name, ip_address, status) # inherites form the parent class (Server)
        self.port = port 

    def start(self):
        self.status = "ONLINE"
        return f"{self.name} server with {self.ip_address} ip address is {self.status} on port {self.port}"

    def to_dict(self):
        d = super().to_dict() # gets the parent dictionary form the parent class 
        d["port"] = self.port # add the port to the dictionary in that class
        return d  # updated one 


class DatabaseServer(Server):
    def __init__(self, name, ip_address, status, db_type):
        super().__init__(name, ip_address, status)
        self.db_type = db_type

    def start(self):
        self.status = "ONLINE"
        return f"{self.name} server with {self.ip_address} ip address {self.db_type} type  is {self.status} "

    def to_dict(self):
        d = super().to_dict()
        d["db_type"] = self.db_type
        return d 


def check_all_servers(servers):
    results = []
    for server in servers:
        print(server.start())
        print(server.get_status())
        results.append(server.to_dict())
        
    return results    


