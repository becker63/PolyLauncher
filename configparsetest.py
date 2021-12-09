import configparser
config = configparser.ConfigParser()
config.read('/usr/share/applications/Alacritty.desktop')
print(config.sections())
print(config['Desktop Entry']['Name'])
