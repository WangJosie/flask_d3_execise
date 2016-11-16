# -*- coding: UTF-8 -*-
#precomputer data to json for flask
#Zhouxi Josie Wang
import json
from sys import argv
from collections import defaultdict
from json import dumps
from collections import OrderedDict


class object:
    def __init__(self):
        self.gi=0 
        self.sda=""
        self.name=""
        self.clusterid=0

    def toJson(self, optfile):
        json.dump(self,optfile, default=lambda  o: o.__dict__,sort_keys=True, indent=4)

#parse and reformate hte original cluster file we have 
def parse_classification(f):
    fn=open(f, "rb") 
    clusterid=0
    clusteritem=defaultdict(list)
    opt=open(f+"_reformate", "wb")
    for line in fn.readlines():
         if line: 
            line=line.rstrip()
            if "cluster" in line:
                #for the line cluster 1, cluster 2, cluster 3
                col=line.split(",")
                protein1=object()
                clusterid=int(col[1].strip())
                protein1.clusterid=clusterid
                print len(col), col [1]
            elif "--" in line:
                col=line.split(",")
                protein1.gi=col[0].strip()
                protein1.sda=col[2].strip()
                pname=col[3].strip()
                pname1=pname.split("[")
                pname=pname1[0].encode('ascii',errors='ignore')
                protein1.name=pname
                print "clusterid:", str(clusterid)
                newline=str(clusterid)+"\t"+str(protein1.gi)+"\t"+protein1.sda+"\t"+protein1.name
                opt.writelines(newline+"\n")
                

    opt.close()
    f2=open(f+"_reformate", "rb")
    for line in f2.readlines():
        line=line.strip()
        row=line.split("\t")
        protein=object()
        print row[0], len(row)
        protein.clusterid=int(row[0])
        protein.gi=row[1]
        protein.sda=row[2]
        protein.name=row[3]
        clusteritem[protein.clusterid].append(protein)

    return clusteritem 

    

#changed the dictionary including the classifications as an output Json file

def dict2Json(clusteritems, output_Tag):
    with open (output_Tag+"_dump","wb") as output:
            json.dump(OrderedDict(clusteritems),   output, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    

if __name__=="__main__":
    f= argv[1] 
    clusteritems=parse_classification(f)
    Tag=f.split(".")[0]
    dict2Json(clusteritems, Tag)


