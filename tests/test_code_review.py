from imagededup.utils import general_utils

file_list = general_utils.generate_files(image_dir='/Users/lucas/Downloads/output_frames', recursive=True)
print(len(file_list))