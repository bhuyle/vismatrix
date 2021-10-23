# vismatrix
### Config
logfile/web.cfg
```
SERVER_IP = 0.0.0.0
SERVER_PORT = 8080
CSV_PATH = ./data/data.csv
TXT_PATH = ./data/data.txt
```
### Annotations
Format: x1,y1,x2,y2,class
```
$ cat data/sample/label/mau-bien-quang-cao-co-khi-825x510.txt
0,0,100,100,1
0,0,200,100,3
0,0,100,200,2
100,100,100,100,1
```
### Setup
```
pip3 install -r requirment.txt
python3 web.py
```
### Web
```
http://<SERVER_IP>:<SERVER_PORT>/thumbnailimg?index=4&imgpath=<Path to images>&labelpath=<Path to annotations>
```
Exp:
```
http://192.168.24.45:8080/thumbnailimg?index=4&imgpath=/host/label/data_mapr/images/&labelpath=/host/label/data_mapr/label/
```
