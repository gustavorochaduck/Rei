import back

print('Welcome to れい(Zero)')
print('-=-'*20)
print('Tools:')
print('[WPA2 Brute Force] - 1')
print('[IP Loockup] - 2')
print('[Speed Test] - 3')
print('-=-'*20)
tool_select = input('Select: ')

if tool_select == 1:
    back.wpa2_brute_force()

elif tool_select == 2:
    back.ip_loockup()

elif tool_select == 3:
    back.speed_test()

