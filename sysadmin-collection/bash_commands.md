# BASH COMMANDS

whoami
history
man
ls
cd
pwd
date
sudo
user
apt-get
apt install
apt update & apt upgrade
mv
rm
cp
mkdir
touch
echo
nano
cut

# change ownership
chmod +x my_file.sh
chmod +777

md5sum 
uname -a

reboot
shutdown -h now

# kill single process
kill <PID process> #use sudo netstat -lntup

# print out
echo "text" >> my_file.txt  

# ping server
ping

# configure network
ifconfig

sudo ss -lntu                            # scan ports info litstn/reciveing
ncat -l 8080 <Num_port>         # scan l=listen
sudo netstat -lntup                   #scan
sudo nmap -n -PN -sT -sU -p- localhost #scan all ports 
nmap -p 1-255 1998.45.7.2

# start servicies
service apache start 
sevice ssh start
service postegresql start  
# stop
service apache stop

# commands to start the server when the machine starts 
systemctl enable ssh 
systemctl enable postegresql


### BASH SCRIPTING ###
# Execute as script
source file.sh

# Assign variables
variabile=k
echo $variabile
> k

# Define function
nameFunc(){
	mkdir -p "$directory_name"
	cd "$directory_name" }


#  call function
nameFunc directory




