from urllib import urlopen as o
proxies = {'http': 'http://bloodsaker97.gmail.com:ei6ybn@gate2.proxyfuel.com:2000'}
lists = open(raw_input('IP list file name: '), 'r').read().split('\n')
for ip in lists:
    print 'Looking', ip
    grab = 'null'
    try:
        grab = o('http://api.hackertarget.com/reverseiplookup/?q=' + ip ,proxies=proxies).read()
    except:
        continue
    if 'error check' in grab:
        print 'Check ip format in input file'
        continue
    if 'No records' in grab:
        print 'No reverse IP record available'
        continue
    grab = grab.split('\n')
    for domain in grab:
        open('grabbedww.txt', 'a+').write(domain + '\n')
