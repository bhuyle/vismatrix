import os
import glob

paths = glob.glob('/host/label/data_mapr/images/*')
out = ''
for path in paths:
    fname = path
    out+=f'{fname} 0 0.5\n'
print(out)
with open('/host/label/vismatrix2/output.txt','w+') as f:
    f.write(out)

