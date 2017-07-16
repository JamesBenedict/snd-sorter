import re, csv, os
from shutil import copyfile
from shutil import rmtree
from glob import glob
# d = csv.reader(open('data.csv', "r", encoding="utf-8", errors ='replace'))
# x = list(d)
# for row in d:
# 	print(row[0])

path = os.getcwd() + '/'

# publications = ['Comercio', 'National Geographic', 'Expresso', 'National Geographic Traveler', 'Centro', 'National Post', 'Wall Street Journal', 'New York Times', 'singles', 'New York Times Magazine', 'Beijing News Agency', 'Omaha World-Herald', 'Bergens Tidende', 'Parool', 'Berliner Morgenpost', 'Philippine Daily Inquirer', 'Bild Am Sonntag', 'Pittsburgh Post-Gazette', 'Boston Globe', 'Plain Dealer', 'Buffalo News', 'Politico Europe', 'Chicago Tribune', 'Politico Magazine', 'China Daily', 'Politiken', 'Clarin', 'Razon de Mexico', 'Colombiano', 'Revista Saude', 'Crains Cleveland Business', 'San Diego Union-Tribune', 'Dagens Nyheter', 'San Francisco Chronicle', 'Dallas Morning News', 'Shabiba', 'Denver Post', 'South China Morning Post', 'Excelsior', 'Stuttgarter Zeitung', 'Financiero', 'Sun Sentinel', 'Folha de Sao Paulo', 'Sunday', 'Galileau', 'Tampa Bay Times', 'Globe and Mail', 'Telegrafo', 'Guardian', 'Times of Oman', 'Gulf News', 'Variety', 'Honolulu Star Bulletin', 'Verdens Gang', 'LEQ Law Enforcement Quarterly', 'Villages Daily Sun', 'Los Angeles Times', 'Voz del Interior', 'Louisville Courier-Journal', 'Washington Business Journal', 'Metro Sao Paulo', 'Washington Post', 'Ming Pao Daily News', 'Welt', 'Minneapolis Star Tribune', 'Welt am Sonntag', 'Nacion', 'Zeit', 'National']
# publications = ['(Colorado Springs) Gazette', '(Lima) Comercio', '(Lisbon) Expresso', '(London) Sunday Times', '(Mexico City) Centro', '(New York) Wall Street Journal', 'Arizona Republic', 'Battle Creek Enquirer', 'Beijing News Agency', 'Bergens Tidende', 'Berliner Morgenpost', 'Bild am Sonntag', 'Boston Globe', 'Buffalo News', 'Business Times', 'Chatelaine', 'Chicago Tribune', 'Chillicothe Gazette', 'China Daily', 'Chronicle of Higher Education', 'Clar�n', 'Colombiano', 'Columbiano', 'Crain�s Cleveland Business', 'Dagens Nyheter', 'Dallas Morning News', 'Denver Post', 'Di Weekend', 'Diario de Hoy', 'Economic Observer', 'Estado de Sao Paulo', 'Excelsior', 'Financiero', 'Folha de S�o Paulo', 'Galileu', 'Globe and Mail', 'Globo', 'Greenville News', 'Guardian', 'Gulf News', 'Helsingin Sanomaat', 'Honolulu Star-Bulletin', 'Indianapolis Star', 'LEQ Law Enforcement Quarterly', 'Los Angeles Times', 'Louisville Courier-Journal', 'Mercury News', 'Metro S�o Paulo', 'Ming Pao Daily News', 'Minneapolis Star Tribune', 'Minneapolis/St. Paul Business Journal', 'Mundo Estranho', 'Naci�n', 'National', 'National Geographic Magazine', 'National Geographic Traveler', 'National Post', 'New York Times', 'New York Times Magazine', 'News Tribune', 'Omaha World-Herald', 'Orlando Sentinel', 'Parool', 'Philippine Daily Inquirer', 'Pittsburgh Post-Gazette', 'Plain Dealer', 'Politico Europe', 'Politico Magazine', 'Politiken', 'Prensa Gr�fica', 'Prensa Libre', 'Provincia', 'Raz�n de M�xico', 'Reporte Indigo', 'Repubblica', 'Revista Sa�de', 'San Diego Union-Tribune', 'San Francisco Business Times', 'San Francisco Chronicle', 'Scenario Magazine', 'Science', 'Seattle Times', 'Shabiba', 'South China Morning Post', 'Stuttgarter Zeitung', 'Sun Sentinel', 'Sunday', 'Svenska Dagbladet', 'Sydney Morning Herald', 'Tagesspiegel', 'Tampa Bay Times', 'Tel�grafo', 'Tennessean', 'Times of Oman', 'Times Polska', 'Today', 'USA Today', 'Variety', 'Verdens Gang', 'Villages Daily Sun', 'Virginian-Pilot', 'Voz del Interior', 'Washington Business Journal', 'Washington Post', 'Welt', 'Welt am Sonntag', 'Zeit', 'Zhejiang Daily']
publications = []
d = csv.DictReader(open('data.csv', 'r', encoding="utf-8",  errors ='replace'))
pdict = {}
# generates list of unique publications
def unique_pubs():
	for row in d:
		if row['PUBLICATION'] not in publications:
			publications.append(row['PUBLICATION']);

def pub_dict():
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


# creates directories for unique pubs
def create_directories():
	os.makedirs(path + 'img/sorted/singles')

	for paper in publications:
		if not os.path.exists(path + 'img/sorted/' + paper):
			os.makedirs(path + 'img/sorted/' + paper)

def num_format(num):
	if len(num) < 4:
		zeros = 4 - int(len(num))
		num = str('0' * zeros) + num
	else:
		num = num 
	return num


def move_imgs():

	pub_dict()

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



		# if ref_num[0:4] 
		# # print(ref_num[0:4])
		# # subdir_files = os.listdir(path)
		# for key, value in pdict.items() :
		# 	if ref_num[0:4] == value:
		# 		print(key, value)
		# 		print()

				# pdict[key] = ref_num

	# print(pub_dict())


	# for row in d:
	# 	folder = os.path.join(path +'img/sorted/' + row['PUBLICATION'])
	# 		# code here
	# 	os.chdir(folder)

	# 	ref = str(row['REF'])
	# 	ref = num_format(ref);
	# 	# print(ref)
	# 	try:
	# 		file = path + '/img/unsorted/' + ref + '.jpg'
	# 		output = os.getcwd() + '/' + ref + '.jpg'
	# 		copyfile(file, output)
	# 		nums.append(ref)

	# 	except FileNotFoundError:
	# 		try:
	# 			# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '']
	# 			# letters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
	# 			letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	# 			for letter in letters:
	# 				letter = letter.upper()
	# 				file = path + '/img/unsorted/' + str(ref) + letter + '.jpg'
	# 				output = os.getcwd() + '/' + str(ref) + letter + '.jpg'
	# 				copyfile(file, output)
	# 				nums.append(ref + letter)
	# 		except:
	# 			print(file, 'file not found')

	# print(len(nums))

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