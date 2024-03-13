class Users:
    user_type = "Free"
    publicity = True
    
    def __init__(self,Nid,alias,name,lastname):
        self.Nid = Nid
        self.alias = alias 
        self.name = name
        self.lastname = lastname
    
    def data_sample(self):
        print