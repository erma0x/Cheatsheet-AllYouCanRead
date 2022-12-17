1. locate proxychain.config
2.  sudo ./../proxychain.config
3. uncomment dynamic_dns
4. comment the other

5. add your chain of proxies in the last row

https 1.1.1.1 8888 username password
socks5 1.1.1.1 8080 username password
http 1.1.1.1 8888 

6.
run:
proxychain <any command> 

