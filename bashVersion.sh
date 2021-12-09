#!/bin/bash

#get bar pid and move to .desktop dir.. 
#theres gotta be a more efficent way to do this
rm -r /tmp/ls.txt
cd /tmp
pid=$(ls | grep "polybar" | sed 's/[^0-9]//g')
cd /usr/share/applications
pidf="%$pid%"


find () {
read name
#get app name and save to txt file for polybar to read
fn=$(ls -1 | grep "$name")
touch /tmp/ls.txt
ls -1 | sed -e 's/\.desktop$//' | sed -e 's/\org.gnome.//' | grep "$name" | head -1 >> /tmp/ls.txt

#display app name output to polybar
polybar-msg -p $pid hook demo 2
}


#exec app
run () {
    path=$(cat $fn | grep "^Exec*" | awk '{gsub("Exec=", "");print}')
    echo $path
    exec $path & sleep 1 && disown
}

find

while true;
do
read VAR
if [ -z $VAR ]; 
then
polybar-msg -p $pid hook demo 1
run 
break 
elif [[ "$VAR" == "q" ]];
then
unset a 
find
fi
done
kill $PPID