import re

# Useful sites:
# 1. Regular expression generator: https://txt2re.com/
# 2. Regular expression tester: https://regex101.com/

print(re.match('baidu', 'www.baidu.com'))

line = "Cats are smarter than dogs"

match_obj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if match_obj:
    print("match_obj.group() : ", match_obj.group())
    print("match_obj.group(0) : ", match_obj.group(0))
    print("match_obj.group(1) : ", match_obj.group(1))
    print("match_obj.group(2) : ", match_obj.group(2))
else:
    print("No match!!")


s = '1102231990xxxxxxxx'

res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)

print(res.groupdict())

uuid = "f47ac10b-58cc-4372-a567-0e02b2c3d479"

match_obj = re.match("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", uuid)

if match_obj:
    print("match_obj.group() : ", match_obj.group())
    print("match_obj.group(0) : ", match_obj.group(0))
else:
    print("No match!!")
