import csv, os
from shutil import copyfile
from shutil import rmtree
from glob import glob

# gets current working directoy, this will save you time typing.
path = os.getcwd() + '/'

# grabs data from same directory as program file
d = csv.DictReader(open('data.csv', 'r', encoding="utf-8",  errors ='replace'))

# global variables 
chapters = []
subchapters = []
chapdict = {}
subdict = {}


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
		
		# below: new_variable = row_in_data['column_header_in_data']. 
		ref = row['REF']
		# returns a formatted number with the utility above
		ref = num_format(ref)
		chapter = row['chapter'] 
		subchapter = row['subchapter']
		
		#creates a list of chapters, 
		#chapter is defined on each pass of the for loop, chapters is the global variable off all chapter
		if chapter not in chapters:
			# I store chapters in both a list and dictonary, the first line below appends the dict, the 2nd appends the list
			chapdict[ref] = chapter
			chapters.append(chapter)
		# does the same thing for subchapters, the len statement is added to weed out subchaters with a length of 0 (blanks)
		if subchapter not in subchapters and len(subchapter) > 0:
			subdict[ref] = subchapter
			subchapters.append(subchapter)
		
		# catches ref not sorted the first time
		if ref not in chapdict:
			chapdict[ref] = chapter

		if ref not in subdict and len(subchapter) > 0:
			subdict[ref] = subchapter
	# print(subchapters)

	return chapters, chapdict, subchapters, subdict

def create_directories():
	# creates the base "chapter" folder if it isn't already there
	if not os.path.exists(path + 'img/chapters/'):
			os.makedirs(path + 'img/chapters/')

	# creates the individual chapter folders, must run the chap_dict function first to get a list of chapters
	for chapter in chapters:
		if not os.path.exists(path + 'img/chapters/' + chapter):
			os.makedirs(path + 'img/chapters/' + chapter)

		# i is ued for the for loop, but would be erased if it were within it
		i = 0
		for subchapter in subchapters:
			# makes folders for each subchapter
			parent_chapter = subchapters[i][0:2]
		# print(parent_chapter)
			i += 1
			
			# print(chapter[0:2])
			if chapter[0:2] == parent_chapter:
				# print(chapter, parent_chapter)
			# navigate into parent chapter
			# if that parent doesn't have a folder called the subfolder
			# make a folder for each subchapter where the parent chapter = current directory
				if not os.path.exists(path + 'img/chapters/' + chapter + '/' + subchapter ):
			 		os.makedirs(path + 'img/chapters/' + chapter + '/' + subchapter)
	# 	# print(chapter) 

def move_imgs():
	# Woooh now onto the actually fun part of sorting

	# gathers all path to all the images held in the img/unsorted directory 
	paths = glob('img/unsorted/*')

	for path in paths:
		# reference is grabbed from the name of the image
		ref = path[13:-4]
		# And then stripped of extra text like ''
		ref_num = ref[0:4] 

		if ref_num in subdict:
			# first I want to sort images into the subfolders

			# this looks ups from the dictonary, dicts are great for recall
			chapter = chapdict[ref_num]
			subchapter = subdict[ref_num]
			# builds an input/output string that is used to sort the image
			file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
			output = os.getcwd() + '/img/chapters/' + chapter + '/' + subchapter + '/' + ref + '.jpg'
			copyfile(file, output)
			# a test that prints out in the terminal.
			print(ref, 'moved')
			pass

		elif ref_num in chapdict:
			# same idea as above
			chapter = chapdict[ref_num]
			file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
			output = os.getcwd() + '/img/chapters/' + chapter + '/' + ref + '.jpg'
			print(ref, 'moved')
			copyfile(file, output)
		
		else:
			# a test to print out everything that didn't move
			print(ref, 'did not move')

chap_dict()
create_directories()
move_imgs()
