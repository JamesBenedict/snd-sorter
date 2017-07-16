import re, csv, os
from shutil import copyfile
from shutil import rmtree
from glob import glob

path = os.getcwd() + '/'

d = csv.DictReader(open('data.csv', 'r', encoding="utf-8",  errors ='replace'))
chapters = []
subchapters = []
chapdict = {}
subdict = {}


# utility 
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
		ref = row['REF']
		ref = num_format(ref)
		chapter = row['chapter'] 
		subchapter = row['subchapter']
		
		#creates a list of chapters 
		if chapter not in chapters:
			chapdict[ref] = chapter
			chapters.append(chapter)
		# does the same thing for subchapters
		if subchapter not in subchapters and len(subchapter) > 0:
			subdict[ref] = subchapter
			subchapters.append(subchapter)
		
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

	# creates the individual chapter folders
	for chapter in chapters:
		if not os.path.exists(path + 'img/chapters/' + chapter):
			os.makedirs(path + 'img/chapters/' + chapter)


		i = 0
		for subchapter in subchapters:
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
	# 	# chapter = subchapters[0][0:2]
	# 	# print(chapter) 
	# 	i += 1
	# 	print(chapter)

def move_imgs():
	paths = glob('img/unsorted/*')

	for path in paths:
		ref = path[13:-4]
		ref_num = ref[0:4] 

		if ref_num in subdict:
			chapter = chapdict[ref_num]
			subchapter = subdict[ref_num]
			file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
			output = os.getcwd() + '/img/chapters/' + chapter + '/' + subchapter + '/' + ref + '.jpg'
			copyfile(file, output)


			print(ref, 'moved')
			pass
		elif ref_num in chapdict:
			# print(ref_num)
			# print(ref)
	
			chapter = chapdict[ref_num]
			file = os.getcwd() + '/img/unsorted/' + ref + '.jpg'
			output = os.getcwd() + '/img/chapters/' + chapter + '/' + ref + '.jpg'
			copyfile(file, output)
		
		else:
			print(ref, 'did not move')


		
	
chap_dict()
create_directories()
move_imgs()
