import re
import os

#filelist = os.listdir(os.getcwd())

img_name = "bcm89530c1_br100_evk_avb-switch_erika_S1.img"
srec_name = img_name.split('.')[0] + '_sw1.srec'

print(srec_name)

#data = "{02:00:00:00:02:00}"

#filename = "swpwer.sre"

#a = re.compile('python$', re.MULTILINE)
#a = re.compile('.+swp.*[.]sre$')
#m = a.findall(data)
#print(m)

#print(type(m))

'''''
for i in m:
    s = '0x%s'%i
    print(s)
'''''

#m = a.sub('0x%d%d', data)
#print(m)

'''''
for filename in filelist:

    m = re.match('.+swp.*[.]sre$', filename)
    if m:
        print('match found' , m.group())

    else:
        #print('No match')
        pass
'''''