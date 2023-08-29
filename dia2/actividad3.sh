#!/bin/bash
i=$(nmap localhost | tail -n 1 | cut -d " " -f 6 | cut -d "(" -f 2) i=$(nmap localhost | tail -n 1 | cut -d " " -f 6 | cut -d "(" -f 2)
echo "host activos: $i"
