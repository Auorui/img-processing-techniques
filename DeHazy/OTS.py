# 一张清晰图对应35张, hazy文件夹下不是放的全部，分成了4个part文件夹, 清洗数据很麻烦
"""
OTS_BETA
	- clear
	- hazy
		- part1
		- part2
		- part3
		- part4
4个part文件夹都归到hazy当中, 总计72135, clear每隔三十五进行一次命名, 若是每张扩充到35就太大了,
所以我准备还是将其写到dataset会更好
"""
import os
from pathlib import Path
from natsort import natsorted
import shutil
from utils import multi_makedirs, SearchFileName

def batch_rename_hazy_file(
	target_path,
	save_path,
	start_index=None,
	file_ext=None,
	search='.jpg',
	preview=True,
):
	file_name_list = []
	for i in range(1, 5):
		target_part_path = os.path.join(target_path, f"part{i}")
		file_name_list.append(SearchFileName(target_part_path, search))
	# print(flattened_list, nums_file)
	start_index = start_index if start_index is not None else 1
	for i in range(1, 5):
		target_part_path = os.path.join(target_path, f"part{i}")
		flattened_list = file_name_list[i - 1]
		nums_file = len(flattened_list)
		for j in range(nums_file):
			file_extension = Path(flattened_list[j]).suffix if file_ext is None else file_ext
			image_file_name = flattened_list[j]
			original_file_path = os.path.join(target_part_path, image_file_name)
			new_file_name = f"{start_index}{file_extension}"
			new_file_path = os.path.join(save_path, new_file_name)
			if not preview:
				shutil.copy(original_file_path, new_file_path)
			print(f"Copied: {original_file_path} -> {new_file_path}")
			start_index += 1

def batch_rename_GT_file(
	target_path,
	save_path,
	start_index=None,
	file_ext=None,
	search='.jpg',
	preview=True,
):
	file_name_list = SearchFileName(target_path, search)
	nums_file=len(file_name_list)
	print(nums_file)
	start_index=start_index if start_index is not None else 1
	for i in range(nums_file):
		file_extension=Path(file_name_list[i]).suffix if file_ext is None else file_ext
		original_file_path = os.path.join(target_path, file_name_list[i])
		new_file_name=f"{start_index}{file_extension}"
		new_file_path=os.path.join(save_path, new_file_name)
		if not preview :
			shutil.copy(original_file_path,new_file_path)
		print(f"{i+1} Copied: {original_file_path} -> {new_file_path}")
		start_index+=35

if __name__=="__main__":
	def process_hazy():
		preview = True
		file_ext = '.png'
		search='.jpg'
		target_hazy_path = r'F:\dataset\Dehazy\OTS_BETA\haze'
		save_hazy_path = r'F:\dataset\Dehazy\OTS_BETA\hazy'

		multi_makedirs(save_hazy_path)
		batch_rename_hazy_file(target_hazy_path, save_hazy_path,
							   file_ext=file_ext, search=search, preview=preview)


	def process_GT():
		preview = False
		file_ext = '.png'
		search='.jpg'
		target_gt_path = r'F:\dataset\Dehazy\OTS_BETA\clear'
		save_gt_path = r'F:\dataset\Dehazy\OTS_BETA\GT'

		multi_makedirs(save_gt_path)
		batch_rename_GT_file(target_gt_path, save_gt_path,
							   file_ext=file_ext, search=search, preview=preview)
	# process_hazy()
	process_GT()












