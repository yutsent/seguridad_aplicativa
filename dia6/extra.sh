#!/bin/bash
sudo apt-get install apache2 -y
sudo systemctl start apache2

sudo a2enmod ssl
sudo systemctl restart apache2
cd /etc/apache2/sites-available
sudo nano default-ssl.conf
sudo a2enmod ssl
sudo systemctl restart apache2
sudo a2ensite default-ssl.conf
sudo systemctl restart apache2
