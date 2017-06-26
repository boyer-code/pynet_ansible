import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    '''this lets us send our commands'''
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out")

def login(remote_conn, username, password):
    '''this is for logging in'''
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    print output

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnet_connect(ip_addr)

    output = login(remote_conn, username, password)
 
    output = send_command(remote_conn, 'terminal len 0')
    print output
    output = send_command(remote_conn, 'show version')  
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()
