from solara import *
from solara.components.file_drop import FileInfo
import os


@solara.component
def Page():

	content,set_content = use_state(b"")
	youfilename,set_youfilename = use_state("")
	yousize,set_yousize = use_state(0)


	def you_file_upload(file:FileInfo):
		# NOW CHANGE filename when you drag file here
		set_youfilename(file['name'])
		set_yousize(file['size'])
		f = file['file_obj']
		set_content(f.read())


	def uploadnow():
		# if IMAGE IN DRAG FOUND 
		if content:
			file_path = os.path.join("public",youfilename)
			with open(file_path,"wb") as file:
				file.write(content)




	with VBox():
		FileDrop(
			label="insert image here",
			on_file=you_file_upload,
			lazy=True
			),
		Button("Upload Image To public folder",
			color="primary",
			on_click=uploadnow
			)
		# IF YOU DRAG FILE THEN SHOW SIZE FILE AND FILE NAME
		if content:
			Info(f"file {youfilename} total size : {yousize} bytes")
