# SOTS 的 indoor, gt图像50张, hazy图像500张, 跟ITS一样, 一张 gt 对应十张合成 hazy
""" https://github.com/Auorui/img-processing-techniques
SOTS/indoor
    - gt
    - hazy
请注意,在去雾当中我个人习惯使用png格式的图片,如果要保留原来格式的,请注意修改格式是否正确
hazy: 1400.png -----> 1400_1.png、1400_2.png、1400_3.png...
"""
import os
from pathlib import Path
import shutil
from utils import multi_makedirs, SearchFileName

def batch_process_SOTS_indoor(
    target_path,
	save_path,
    file_ext=None,
    preview=True,
):
	file_name_list = SearchFileName(target_path)
	nums_file = len(file_name_list)

	for i in range(nums_file):
		file_extension = Path(file_name_list[i]).suffix if file_ext is None else file_ext
		image_file_name = file_name_list[i]

		original_file_path = os.path.join(target_path, image_file_name)

		for j in range(1, 11):  # 复制10份，从1到10
			new_file_name = f"{file_name_list[i].split('.')[0]}_{j}{file_extension}"
			new_file_path = os.path.join(save_path, new_file_name)

			if not preview:
				shutil.copy2(original_file_path, new_file_path)
			print(f"Copying {original_file_path} to {new_file_path}")



if __name__=="__main__":
	# 后缀名, 如果为None, 就使用原来的后缀
	file_ext = '.png'
	# 建议先进行预览 True, 避免出错, 确定没问题后改为False
	preview = False

	original_path = r'F:\dataset\Dehazy\SOTS\indoor\gt'
	save_path = r'F:\dataset\Dehazy\SOTS\indoor\GT_1'
	multi_makedirs(save_path)
	batch_process_SOTS_indoor(original_path, save_path, file_ext=file_ext, preview=preview)