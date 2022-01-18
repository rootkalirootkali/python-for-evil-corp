#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("                Welcome, to the fsociety networking tool   ")
print("____________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("___________________________________________________________________________")
print("    .o88o.                               o8o              __              ")
print("    888  '"                               "'             oo8               ")
print("  o888oo   .oooo.o  .ooooo.    .ooooo.   ooo   .ooooo..88oo888oo oo     oo ")
print("    888    d88(     d8888d88  '888'   '  888  d88'  8b   888      88    80 ")
print("    888    '88b    888  '888  888       '888 '8888oo888' '888     `88. 88  ")
print("    888     o88b  '888   88   888   .o8  888  888    .o   888 .     888d   ")   
print("   o888o   888P'  `Y8bod8P'   `Y8bod8P' o888o `Y8bod8P'   '888'     d8d    ")
print("                                                                  .o88     ") 
print("                                                                  '888     ")
print("                                                                  tyler    ")
print("____________________________________________________________________________")
print("____________________________________________________________________________")
print("____________________________________________________________________________")
print("____________________________________________________________________________")

ip_addr = input("Please enter the address/ubnet you want to scan: ")


print("This is your IP ")

print("ARE YOU SURE its correct: ", ip_addr)
type(ip_addr) 

resp = input("""\nPlease eventer the type of DDOS attack you want to run
                 1)SYN Flood
                 2)UDP Overload
                 3)Log4j Vulnerabitility Scanner
                 4)Darknet Identifier""")
print ("Great Choice: ", resp)


if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports:", scanner[ip_addr]['tcp'].keys())

