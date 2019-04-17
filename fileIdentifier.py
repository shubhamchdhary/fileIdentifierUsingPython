import os

audio_ext = ['mp3','wav']
video_ext = ['mp4','flv','mkv','avi']
doc_ext = ['pdf','doc','docx','xls','ppt','txt']
photo_ext = ['jpg','jpeg','png','img','tmb']

file_path = input('Enter the file path : ')
dict1 = {}

if os.access(file_path,os.F_OK) == True:
	file_list = os.listdir(file_path)
	for file in file_list:
                #checking_folder = os.path.isdir(file)
		print(file)
                #print(checking_folder)
		if os.path.isdir(file) == False:
			filename,fileext = file.split('.')
			if fileext in audio_ext:
				update1 = {file:'It is an audio file.'}
				dict1.update(update1)
			elif fileext in video_ext:
				update2 = {file:'It is a video file.'}
				dict1.update(update2)
			elif fileext in doc_ext:
				update3 = {file:'It is a document file.'}
				dict1.update(update3)
			elif fileext in photo_ext:
				update4 = {file:'It is a picture.'}
				dict1.update(update4)
			else:
				update5 = {file:'It is a miscellenious file.'}
				dict1.update(update5)

		else:
			update6 = {file:'It is a folder.'}
			dict1.update(update6)
	print(dict1)
else:
	print(f'{file_path} does not exist.')
