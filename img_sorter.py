import re, csv, os
from shutil import copyfile
from shutil import rmtree
from glob import glob

# The chapter sorter is what is actually used

path = os.getcwd() + '/'
# global variable used throughout program
publications = []
pdict = {}


# grabs data
d = csv.DictReader(open('data.csv', 'r', encoding="utf-8",  errors ='replace'))

def unique_pubs():
	# generates list of unique publications
	for row in d:
		if row['PUBLICATION'] not in publications:
			publications.append(row['PUBLICATION']);

def pub_dict():
	# generates a dictonary with the publication and all reference numbers for it. 
	# In english: it tells me all the images made by a publication
	for row in d:
		pub = row['PUBLICATION'] 
		ref = row['REF']
		ref = num_format(ref)
		
		if ref not in pdict:
			pdict[ref] = []

		if pub not in pdict:
			# pdict[ref].append(pub)
			pdict[ref] = pub
	# print(pdict)
	return pdict


def create_directories():
	# creates directories for unique pubs
	os.makedirs(path + 'img/sorted/singles')

	for paper in publications:
		if not os.path.exists(path + 'img/sorted/' + paper):
			os.makedirs(path + 'img/sorted/' + paper)

def num_format(num):
	# utility to make all numbers four digits, 1 becomes 0001
	if len(num) < 4:
		zeros = 4 - int(len(num))
		num = str('0' * zeros) + num
	else:
		num = num 
	return num


def move_imgs():

	pub_dict()
	# creates the dictonary, defined above

	paths = glob('img/unsorted/*')
	for path in paths:
		ref_num = path[13:-4]

		if ref_num[0:4] in pdict:
			publication = pdict[ref_num[0:4]]
			file = os.getcwd() + '/img/unsorted/' + ref_num + '.jpg'
			output = os.getcwd() + '/img/sorted/' + publication + '/' + ref_num + '.jpg'
			
			print(file, output)
			copyfile(file, output)

		else:
			print(ref_num, 'error moving')



def group_singles():
	total_images =[ ]
	paths = glob('img/sorted/*/')
	for path in paths:
		# folder = os.path.join(path +'img/sorted/' + row['PUBLICATION'] + '/')
		# print(folder, os.listdir(folder))
		# print(path, os.path.getsize(path))

		subdir_files = os.listdir(path)
		if len(subdir_files) == 1:
			image = subdir_files[0]
			total_images.append(image)
			try:

				file = os.getcwd() + '/' + path + image
				output =  os.getcwd() + '/img/sorted/singles/'  + image
				copyfile(file, output)
				print(file, output)
				os.remove(file)
			except:
				print(file +' not moved ')
				pass
	# 		# rmtree(path)
	# 		# print(path)
		else:
			for i in subdir_files:
				total_images.append(i) 

	return total_images


def remove_empty():
	paths = glob('img/sorted/*/')
	for path in paths:
		if len(os.listdir(path)) == 0:
			# print(path)
			rmtree(path)

def check_img():
	total_sorted = group_singles()
	path = os.getcwd() + '/img/unsorted/'
	total_unsorted = os.listdir(path)
	
	diff = list(set(total_unsorted) - set(total_sorted))


	format_sort = 'The sorted folder contains ' + str(len(total_sorted)) + ' images' + '\b'
	format_unsort = 'The unsorted folder contains ' + str(len(total_unsorted)) + ' images'
	diff = list(set(total_unsorted) - set(total_sorted))
	# diff2 = list(set(total_sorted) - set(total_unsorted))

	print(format_sort)
	print(format_unsort)
	print(diff)
	# except:
	# 	format_sort = "didn't move"
	# 	format_unsort = "didnt move"
	# 	diff = 'nah'

	# for image in diff:
		# print(image)
		# for row in d:
			# if row['REF'] == int(item[0:3])
	# return total_sorted, total_unsorted
	# print(format_unsort) 
	# print(format_sort)
	# print(diff)

# unique_pubs()
# create_directories()
# pub_dict()

# move_imgs()
# group_singles()
# remove_empty()
check_img()


# num_format('2000')