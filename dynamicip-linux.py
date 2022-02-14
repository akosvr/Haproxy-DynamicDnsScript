import dns
import dns.resolver
import time
import os


# Target address
target = "google.com"
# OS command
commandifchanged = "/etc/init.d/haproxy reload"

print('Dynamic ip script by Akos started!')
firstresult = dns.resolver.query(target, 'A')
for ipval in firstresult:
    firstresultip = ipval.to_text()

print('If ',target,' changed you will see something like this!')
print('Ip changed!', 'lastip', ' => ', 'currentip')
print('First ip registered, ', firstresultip, ' waiting for change...')

while True:
        try:
                time.sleep(1)
                result = dns.resolver.query(target, 'A')
                for ipval in result:
                        currentresultip = ipval.to_text()
                if(not (currentresultip == firstresultip)):
                        print('Ip changed!', firstresultip, ' => ', currentresultip)
                        # Run commands here if ip is changed
                        os.system(commandifchanged)
                        firstresult = dns.resolver.query(target, 'A')
                        for ipval in firstresult:
                                firstresultip = ipval.to_text()
        except:
                print('Failed to get dns addresses!')
