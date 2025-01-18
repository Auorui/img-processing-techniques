""" 数据集中清晰图共492张，合成图共500张，合成图中有一些重合的，我一张一张找出来的。所以修正过后共计492对。
SOTS/indoor
    - GT
    - hazy
"""
import os
from pathlib import Path
import shutil
from utils import multi_makedirs, SearchFileName


def batch_process_SOTS_outdoor(
    target_path,
	save_path,
	start_index=1,
    file_ext=None,
	search='.jpg',
    preview=True,
):
	file_name_list = SearchFileName(target_path, search)
	nums_file = len(file_name_list)
	start_index=start_index if start_index is not None else 1
	for i in range(nums_file):
		file_extension = Path(file_name_list[i]).suffix if file_ext is None else file_ext
		image_file_name = file_name_list[i]
		original_file_path = os.path.join(target_path, image_file_name)
		new_file_name = f"{start_index}{file_extension}"
		new_file_path = os.path.join(save_path, new_file_name)
		if not preview :
			shutil.copy(original_file_path, new_file_path)
		print(f"Copied: {original_file_path} -> {new_file_path}")
		start_index += 1


if __name__=="__main__":
	# 建议先进行预览 True, 避免出错, 确定没问题后改为False
	preview = False

	target_path = r"F:\dataset\Dehazy\SOTS\outdoor"
	save_path = r'F:\dataset\Dehazy\SOTS\outdoor\cache'
	save_gt_path = os.path.join(save_path, 'GT')
	save_hazy_path = os.path.join(save_path, 'hazy')
	multi_makedirs(save_hazy_path, save_gt_path)

	target_gt_path=os.path.join(target_path, 'gt')
	target_hazy_path = os.path.join(target_path, 'hazy')
	batch_process_SOTS_outdoor(target_gt_path, save_gt_path, file_ext='.png',
							   search='.png', preview=preview)
	batch_process_SOTS_outdoor(target_hazy_path, save_hazy_path, file_ext='.png',
							   search='.jpg', preview=preview)
