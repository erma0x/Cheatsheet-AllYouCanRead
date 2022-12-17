How to Detect if Your Linux System has been Hacked

w
top
who
last
su <user>
history

iftop 
sudo iftop -i <interface>

netstat -la

top

lsof  -p <PID>

#The command lsof allows to see what files are opened and their associated processes.
#for suspicious processes
ps -axu
sudo chkrootkit
