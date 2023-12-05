import pickle
import os

class pickle_db:
    def __init__(self, name):
        self.name = name
        if os.path.isfile(name) == False:
            records = [] 
            with open(name, 'wb') as handle:
                pickle.dump(records, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(name, 'rb') as handle:
            records = pickle.load(handle)
        self.records = records
       
       
    def insert(self,record=dict):
        with open(self.name, 'rb') as handle:
            records = pickle.load(handle)
        records.append(record)
        with open(self.name, 'wb') as handle:
            pickle.dump(records, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def getall(self):
        with open(self.name, 'rb') as handle:
            records = pickle.load(handle)
        return records
    
    def clearall(self):
        records = [] 
        with open(self.name, 'wb') as handle:
            pickle.dump(records, handle, protocol=pickle.HIGHEST_PROTOCOL)


        



         
         

     