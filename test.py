import os
import pickle

path = os.path.join(os.getcwd(),"Districts_Dicts","NYC GEOG DIST # 1 - MANHATTAN .dict")

dist_dict = {}

with open(path, 'rb') as fp:
    dist_dict['test'] = pickle.load(fp)

print(dist_dict)