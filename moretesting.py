import glob
import io
import tempfile
import configparser
import re
config = configparser.RawConfigParser()

print(config.sections())
input = input()
cinput = input.capitalize()

path = glob.glob(f'/usr/share/applications/*.desktop')
print(path)
names = []
for e in path:
    config.read(e)
    name = (config['Desktop Entry']['Name'])
    a = f'{name }={e}'
    print(a)
    names.append(a)

snames = '\n'.join(names)
print(snames)
for line in snames.split('\n'):
    if cinput in line:
        print(line)
        #delete appname and delimiter so i can get the  path
        t = re.sub(r'^.*?=', '=', line)
        gpath = t.replace("=", "") 
        print(gpath)
        break

def run(rpath):
    config.read(rpath)
    exec = (config['Desktop Entry']['Exec'])
    print(exec)

run(gpath)
    
