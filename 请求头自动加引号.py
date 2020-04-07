import re

headers="""

"""

pattern='^(.*?):(.*)$'

for line in headers.splitlines():
    line=line.replace(' ','')
    print(re.sub(pattern,'\'\\1\':\'\\2\',', line))
