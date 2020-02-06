import csv, os
from shutil import copyfile
from shutil import rmtree
from glob import glob

print('This was only tested on a Mac using python 3.0+, running it on a pc might run into errors')
print('If you run into problems with the version of your python, download a lastest version here https://www.python.org/downloads/ or contact me to port this to python 2.7 (the version default for OSX)')
print("Don't hesitate to reach out, even years later, I'm always here to help")
print('*********************************************')

# return confirm_info

# gets current working directoy this will save you time typing.
path = os.getcwd() + '/'


# global variables 
chapters = []
subchapters = []
chapdict = {}
subdict = {}
data_name = ""
ref_num = ""
chap_name = ""
subchap_name = ""
d = ""



# utility to make numbers consistent, if '20' goes in '0020' comes out.
def num_format(num):
	if len(num) < 4:
		zeros = 4 - int(len(num))
		num = str('0' * zeros) + num
	else:
		num = num 
	return num

# creates a list of unique chapters
def chap_dict():
	for row in d:
		# for each line the database writes its ref, chapter and subchapter into list for the program to use elsewhere 
		# print(row)
		# below: new_variable = row_in_data['column_header_in_data']. 
		
		ref = row['REF']
		# returns a formatted number with the utility above
		
		ref = num_format(ref)
		chapter = row[chap_name] 
		subchapter = row[subchap_name]
		
		#creates a list of chapters, 
		#chapter is defined on each pass of the for loop, chapters is the global variable off all chapter
		if chapter not in chapters:
			# print(chapter)
			chapdict[ref] = chapter
			chapters.append(chapter)
		# # does the same thing for subchapters, the len statement is added to weed out subchaters with a length of 0 (blanks)
		# if subchapter not in subchapters and len(subchapter) > 0:
		# 	subdict[ref] = subchapter
		# 	subchapters.append(subchapter)
		# 	# print(subchapter)
		
		# catches ref not sorted the first time
		if ref not in chapdict:
			chapdict[ref] = chapter

		# if ref not in subdict and len(subchapter) > 0:
		# 	subdict[ref] = subchapter
	# print(subchapters)

	# return chapters, chapdict, subchapters, subdict
	return chapters, chapdict

def create_directories():
	# creates the base "chapter" folder if it isn't already there
	if not os.path.exists(path + 'img/chapters/'):
			os.makedirs(path + 'img/chapters/')

	# creates the individual chapter folders, must run the chap_dict function first to get a list of chapters
	for chapter in chapters:
		print(chapter)
		if not os.path.exists(path + 'img/chapters/' + chapter):
			os.makedirs(path + 'img/chapters/' + chapter)

		# i is ued for the for loop, but would be erased if it were within it
	# 	i = 0
	# 	for subchapter in subchapters:
	# 		# print(subchapter)
	# 		# makes folders for each subchapter
	# 		parent_chapter = subchapters[i][0:2]
	# 	# print(parent_chapter)
	# 		i += 1
			
	# 		# print(chapter[0:2])
	# 		if chapter[0:2] == parent_chapter:
	# 			# print(chapter, parent_chapter)
	# 		# navigate into parent chapter
	# 		# if that parent doesn't have a folder called the subfolder
	# 		# make a folder for each subchapter where the parent chapter = current directory
	# 			if not os.path.exists(path + 'img/chapters/' + chapter + '/' + subchapter ):
	# 		 		os.makedirs(path + 'img/chapters/' + chapter + '/' + subchapter)
	# # 	# print(chapter) 

def move_imgs():
	# Woooh now onto the actually fun part of sorting

	# gathers all path to all the images held in the img/unsorted directory 
	# paths = glob('img/unsorted/*')
	paths = glob('img/*')

	print(chapdict)
	for path in paths:
		# print(path)
		# reference is grabbed from the name of the image
		ref = path.replace("img/", "")
		# print(ref)
		# And then stripped of extra text like ''
		ref_number = ref[0:4]
		# print(ref_number) 


		# if ref_number in chapdict:
		# 	# first I want to sort images into the subfolders

		# 	# this looks ups from the dictonary, dicts are great for recall
		# 	chapter = chapdict[ref_num]
		# 	subchapter = subdict[ref_num]
		# 	# builds an input/output string that is used to sort the image
		# 	# file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
		# 	file = os.getcwd() + '/img/' + ref + '.jpg'

		# 	output = os.getcwd() + '/img/chapters/' + chapter + '/' + subchapter + '/' + ref + '.jpg'
		# 	copyfile(file, output)
		# 	# a test that prints out in the terminal.
		# 	print(ref, 'moved')
		# 	pass

		# print(chapdict)
		# print(ref_number)
		if ref_number in chapdict:
			# print(ref_number)
			# same idea as above
			chapter = chapdict[ref_number]
			# file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
			file = os.getcwd() + '/img/' + ref
			output = os.getcwd() + '/img/chapters/' + chapter + '/' + ref
			# print(ref, 'moved')
			copyfile(file, output)
		
		else:
			# a test to print out everything that didn't move
			print(ref, 'did not move')



# def prompt():
	# print('First: Save your excel data as a CSV into the same directory as this program')
	# data_name = input('What is the exact name of your CSV data? Include .csv in your name: ')
	# ref_num = input('\nWhat is the column header for your reference number?: ')
	# chap_name = input('\nWhat is the column header for the chapter column?:  ')
	# subchap_name = input('\nWhat is the column header for the subchapter column?: ')
	# confirm_message = '\n So in the '+ data_name+ ' file the reference number is stored under '+ ref_num+ ' and the chapter is stored under '+ chap_name+ ' and the subchapter is stored under '+ subchap_name + ' and these are the correctly capitalized and is in the same folder as this program file? Type "yes" to contiune, and "no" to restart the questions: '
	# confirm_info = input(confirm_message)
	

# chap_dict()
# create_directories()
# move_imgs()

# confirm_info = "no"
def start_program():
	global data_name
	global ref_num
	global chap_name
	global subchap_name
	
	data_name = 'snd39data.csv'
	ref_num = "REF"
	chap_name = "General Category Name"
	subchap_name = "Specific Category Name"
	confirm_info = 'yes'
	img_folder = 'images39'
	
	if confirm_info == 'yes':
		# grabs data from same directory as program file
		global d
		d = csv.DictReader(open(data_name, 'r', encoding="utf-8-sig",  errors ='replace'))
		# for row in d:
		# 	print(row)
		# 	break
		chap_dict()
		create_directories()
		move_imgs()
	else:
		start_program()

start_program()





# ask for variables
# sort images
# create csv of sorted/unsorted images

