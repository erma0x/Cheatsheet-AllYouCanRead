# Ubuntu / Debian
# CLEANUP CACHE 
su -sh /var/cache/apt/archives  
sudo apt-get autoremove --purge

# CLEANUP PACKAGES
sudo apt-get remove package-name1 package-name2

