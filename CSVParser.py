import json
import csv
import sys
import os

class CSVParser():
    def __init__(self):
        pass    

    def humanbytes(self,B):
    #Return the given bytes as a human friendly KB, MB, GB, or TB string
        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2) # 1,048,576
        GB = float(KB ** 3) # 1,073,741,824
        TB = float(KB ** 4) # 1,099,511,627,776

        if B < KB:
            return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B/KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B/MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B/GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B/TB)
            
    def resource_path(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def do_query(self,name):
        search = name
        body={}
        n=0
        file_path = self.resource_path('dump_release_tntvillage_2019-08-30.csv')
        with open(file_path, mode='r',encoding="utf8") as csv_file: #TODO add path to your csv file if different name or different folder
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                tit = row["TITOLO"].lower() 
                if tit.startswith(search.lower()) or search.lower() in tit:
                    n=n+1
                    dim = self.humanbytes(row["DIMENSIONE"])
                    magnet = "magnet:?xt=urn:btih:" + row["HASH"]
                    body[n]= {
                        "titolo": row["TITOLO"],
                        "descrizione": row["DESCRIZIONE"],
                        "dimensione" : dim,
                        "magnet": magnet
                    }
        return body