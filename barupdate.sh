cd /tmp
pid=$(ls | grep "polybar" | sed 's/[^0-9]//g')
polybar-msg -p $pid hook demo 2
