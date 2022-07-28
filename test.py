import os
import subprocess
from pathlib import Path
import sys
import cmd1

#Example project = bt_soc_thunderboard
#ex_p_name = input("Enter example project name that you want to use: ") 

set_ex_p = 'C:\\Users\\lakarkee\\SimplicityStudio\\SDKs\\gecko_sdk_4\\app\\bluetooth\\example'
#set_ex_p = f'C:/Users/lakarkee/SimplicityStudio/SDKs/gecko_sdk_4/app/bluetooth/example/{ex_p_name}/{ex_p_name}_brd4184a.slcp'
set_dst_dir = 'C:\\Users\\lakarkee\\SimplicityStudio\\v5_workspace\\'


ex_list=(os.listdir(set_ex_p))
for each_ex in ex_list:
	print(each_ex)
print("Commander example")   
s1 = cmd1.SimplicityCommander()
l1 = s1.get_serialno()
l2 = s1.get_boards()

Jlink_board ={l1[i]: l2[i] for i in range(len(l1))}
print(f'JLink: Board \n ',Jlink_board)

#print('J Link Serial No: ', s1.get_serialno())

#print('Boards: ',s1.get_boards())


f_name = input("Enter Project Name that you want to create : ")
sel_proj_ex=input('Enter the example that you want to create: ')


sel_proj_dir=os.path.join(set_ex_p,sel_proj_ex)
if os.path.exists(sel_proj_dir):
	print(sel_proj_dir)
else:
	print('Plz select right example')
	sys.exit()


for r,d,f in os.walk(sel_proj_dir):
	slcp_f=[]
	for each_f in f:
		if each_f.endswith('.slcp'):
			#slcp_f.append(each_f)
			print(each_f)

sel_file=input('Enter .slcp proj file that you want to create: ')
proj_filep=os.path.join(sel_proj_dir,sel_file)
if os.path.isfile(proj_filep):
	print(f'path for project that you want to create is: {proj_filep}')
else:
	print('path to proj not found')

'''

promt_proceed = input('Enter "Y/y" to continue "N/n" to exit: ')
if promt_proceed == 'N' or 'n':
	sys.exit()
else:
'''
#path = 'C:/Users/lakarkee/SimplicityStudio/SDKs/gecko_sdk_4/app/bluetooth/example/'

slc_g = 'slc generate'
subprocess.run(f'{slc_g} {proj_filep} -np -d {set_dst_dir}{f_name} -name={f_name} --with brd4184a', shell=True)

os.chdir(f'C:\\Users\\lakarkee\\SimplicityStudio\\v5_workspace\\{f_name}')

subprocess.call(f'make -f {f_name}.Makefile')
subprocess.call(f'commander flash build/debug/{f_name}.hex --serialno 440190435')
