import os
import subprocess
import time
import sys

print('*'*40)
print('Note : You can search any file in your computer just by drive!!!!!!!')
print("Welcome to the file searching")
print('*'*30)


def search_file():
	files = []
	try:
		search_file = input('Enter the file name you want to search  : ')
		choose = input('Do you want to give any directory or search in whole drive y or n  : ')
		choose = choose.lower()
		if choose=='y':

			dirs = input('Enter the directory you want to search : ')
			if len(dirs)>1:
				print('*'*40)
				print('Please enter only directory!!!!')
				return 0
			print('searching start at',time.ctime())
			#local_time = time.localtime()[5]
			dirs = dirs+':'
			print('*'*40)
			try:
				for loc,fol,file in os.walk(dirs):
					if search_file in file:
						files.append(loc)
				if not files:
					print('*'*40)
					print("Sorry file does not exist!!!!!!")
					#real_time = time.localtime()[5]
					print('*'*40)
					#print("Total time : ",real_time-local_time,"sec")
				else:
					for i in files:
						print("Location of files : ",i)
						s = os.stat(i+'/'+search_file)
						print("size  of the file",s.st_size/2**20,'MB')
						print('*'*40)
					print("Total search result",len(files))
					files.clear()

			except KeyboardInterrupt as e:
				print('*'*40)
				print('Exiting')
				return 0

			except Exception as e:
				print('*'*40)
				print("Invalid directory!!!!!")
				return 0

		elif choose=='n':
			print('*'*40)
			print('searching start at',time.ctime())
			local_time = time.localtime()[5]
			re = subprocess.getoutput('wmic logicaldisk get caption')
			a=[]
			for i in range(1,len(re)):
				if ord(re[i])>=65 and ord(re[i])<=90:
					a.append(re[i]+':')
			#print(a)
			for i in range(len(a)):
				for loc,fol,file in os.walk(a[i]):
					if search_file in file:
						files.append(loc)
			if not files:
				print('*'*40)
				print("Sorry file does not exist!!!!!!")
				real_time = time.localtime()[5]
				print('*'*40)
				#print("Total time : ",real_time-local_time,"sec")
			else:
				for i in files:
					print("Location of files : ",i)
					s = os.stat(i+'/'+search_file)
					print("size  of the file",s.st_size/2**20,'MB')
					print('*'*40)
				print("Total search result",len(files))
				files.clear()


		else:
			print('*'*40)
			print("Please enter valid option!!!!")

	except KeyboardInterrupt as e:
		print('*'*40)
		print('Exiting')
		sys.exit(0)

	except Exception as e:
		print('*'*40)
		sys.exit(0)
		print("Something wrong")

def search_folder():
	folds = []
	try:
		search_file = input('Enter the folder name you want to search: ')
		choose = input('Do you want to give any directory or search in whole drive y or n: ')
		choose = choose.lower()
		if choose=='y':
			dirs = input('Enter the directory you want to search: ')
			print('*'*40)
			print('searching start at',time.ctime())
			local_time = time.localtime()[5]
			if len(dirs)>1:
				print('*'*40)
				print('Please enter only directory!!!!')
				return 0
			dirs = dirs+':'

			try:
				for loc,fol,file in os.walk(dirs):
					if search_file in fol:
						folds.append(loc)
				if not folds:
					print('*'*40)
					print("Sorry the file does exist!!!!!!")
					real_time = time.localtime()[5]
					print('*'*40)
					print("Total time : ",real_time-local_time,"sec")
				else:
					for i in folds:
						print()
						print("Location of the folder : ",i)
					real_time = time.localtime()[5]
					print('*'*40)
					print("Total time : ",real_time-local_time,"sec")
					folds.clear()

			except KeyboardInterrupt as e:
				print('*'*40)
				print('Exiting')
				return 0

			except Exception as e:
				print('*'*40)
				print("Invalid directory!!!!!")
				return 0
		elif choose=='n':
			print('*'*40)
			print('searching start at',time.ctime())
			local_time = time.localtime()[5]
			re = subprocess.getoutput('wmic logicaldisk get caption')
			a=[]
			for i in range(1,len(re)):
				if ord(re[i])>=65 and ord(re[i])<=90:
					a.append(re[i]+':')
			for i in range(len(a)):
				for loc,fol,file in os.walk(a[i]):
					if search_file in fol:
						folds.append(loc)
			if not folds:
				print('*'*40)
				print("Sorry the file does exist!!!!!!")
				real_time = time.localtime()[5]
				print("Total time : ",real_time-local_time,"sec")
			else:
				for i in folds:
					print('*'*40)
					print("Location of the folder : ",i)
				real_time = time.localtime()[5]
				print("Total time : ",real_time-local_time,"sec")
				folds.clear()
		else:
			print('*'*40)
			print("Please enter valid option!!!!")

	except KeyboardInterrupt as e:
				print('Exiting')
				return 0

	except Exception as e:
		print('*'*40)
		return 0





while(1):

	try:
		print('*'*40)
		n=int(input('Please select want you to search for\n1:File\n2:Folder\n3:Exit\n'))

		if n==1:
			search_file()
			print('*'*40)
			more = input('Search for more files y or n : ')
			try:
				if more.lower()=='y':
					continue
				elif more.lower()=='n':
					print('*'*40)
					print("Thanks for using our service!!!!!!")
					sys.exit(0)
				else:
					print('*'*40)
					print("Invalid choice!!!!!!")
					continue
			except Exception as e:
				print("Something wrong!!!!!!!")
		elif n==2:
			search_folder()
			more = input('Search for more files y or n : ')
			try:
				if more.lower()=='y':
					continue
				elif more.lower()=='n':
					print('*'*40)
					print("Thanks for using our service")
					sys.exit(0)
				else:
					print('*'*40)
					print("Invalid choice!!!!!!")
			except Exception as e:
				print('*'*40)
				print('Something gone wrong!!!')
				continue
		elif n==3:
			print('*'*40)
			print("Thanks for using our service")
			sys.exit(0)
		else:
			print('Please select valid option')
			continue
	except KeyboardInterrupt as e:
		print("Exiting")
		sys.exit(0)
	except Exception as e:
		print('*'*40)
		print("Please enter valid choice")
		continue