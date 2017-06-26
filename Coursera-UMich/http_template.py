def integer_check(user_supplied_number): #this is a function to ensure that the user is actually entering a number
    while True:
        try: 
            user_supplied_number = int(user_supplied_number)
            if user_supplied_number > 0:
                return user_supplied_number
            else:
                print 'that will not work'
                user_supplied_number = raw_input('please enter a valid integer ')
                continue
        except:
            print 'that will not work'
            user_supplied_number = raw_input('please enter a valid integer ')
            continue

def server_names_and_ips_loop(server_variable):   #this function will ask users for server names and IPs, then add them to a list...we'll later read from the list to create our pools
    serverList = [] #reset the list that we update in the loop...this allows us to reuse the function with fresh lists per DC
    while server_variable > 0:
        #print server_variable
		serverName = raw_input('What is the server name? ')
		serverIP = raw_input('What is the server IP? ')
		serverName = str(serverName)
		serverIP = str(serverIP)
		serverList.append(serverName)
		serverList.append(serverIP)
		server_variable -= 1
        #print serverList
        #print serverIPList
    return serverList


#appID = raw_input('What is your app ID? ')
#appID = integer_check(appID)
#print 'AppID is',appID
#path = raw_input('What is your probe path? ')
#print 'path is',path
backend80Port = raw_input('What is your backend 80 port? ')
#backend80Port = integer_check(backend80Port)
#print '80 redirects to',backend80Port
#backend443Port = raw_input('What is your backend 443 port? ')
#backend443Port = integer_check(backend443Port)
#print '443 redirects to',backend443Port
pdc1ServerCount = raw_input('How many PDC1 servers do you have? ')
pdc1ServerCount = integer_check(pdc1ServerCount)
#pdc3ServerCount = raw_input('How many PDC3 servers do you have? ')
#pdc3ServerCount = integer_check(pdc3ServerCount)
serverListPDC1 = []
#serverListPDC3 = []
appName = raw_input('What is your application name? ')
#appFQDN = raw_input('What is your FQDN? ')
#vip1 = raw_input('What is your first VIP? ')
#vip2 = raw_input('What is your second VIP? ')
serverListPDC1 = server_names_and_ips_loop(pdc1ServerCount)
#serverListPDC3 = server_names_and_ips_loop(pdc3ServerCount)
#print 'modify ltm profile',appName,'-ssl-profile something I don\'t remember without looking at my notes'
#modify the below to add the servers to the pools once we write the for/while loops to get input for each server name
print 'create ltm pool '+appName+'-'+backend80Port+'-pool members add '+serverListPDC1[0]+':'+backend80Port+' { address ',serverListPDC1[1],' } ',serverListPDC1[2],'\b:',backend80Port,'\b\{ address',serverListPDC1[3],'\}'
