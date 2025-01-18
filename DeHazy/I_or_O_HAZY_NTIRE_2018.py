# 下载之后，文件夹名为：I-HAZY NTIRE 2018, 这里我们手动改为I_HAZY_NTIRE_2018
# O-HAZY NTIRE 2018, 这里我们手动改为O_HAZY_NTIRE_2018
""" https://github.com/Auorui/img-processing-techniques
I_HAZY_NTIRE_2018
        - GT
        - hazy
O_HAZY_NTIRE_2018
        - GT
        - hazy
请注意,在去雾当中我个人习惯使用png格式的图片,如果要保留原来格式的,请注意修改格式是否正确
01_indoor_hazy.jpg -----> 1.png
"""
import os
from pathlib import Path
from natsort import natsorted
import shutil
from utils import multi_makedirs
            
def batch_process_I_HAZY_NTIRE_2018(
    target_path,
    save_path,
    start_index=None,
    file_ext=None,
    preview=True,
):
    file_list = natsorted(os.listdir(target_path))
    nums_file = len(file_list)
    start_index = start_index if start_index is not None else 1
    for i in range(nums_file):
        file_extension = Path(file_list[i]).suffix if file_ext is None else file_ext
        new_file_name = f"{start_index}{file_extension}"
        start_index += 1
        new_file_path = os.path.join(save_path, new_file_name)
        file_path = os.path.join(target_path, file_list[i])
        if not preview:
            shutil.copy(file_path, new_file_path)
        print(f"Copied: {file_path} -> {new_file_path}")

if __name__=="__main__":
    # 建议先进行预览 True, 避免出错, 确定没问题后改为False
    preview = False
    # 起始数字, 如果为None, 默认从 1 开始
    start_index = 1
    # 后缀名, 如果为None, 就使用原来的后缀
    file_ext = '.png'
    # # 目标文件夹路径 I_HAZY
    # target_path = r'F:\dataset\Dehazy\I_HAZY_NTIRE_2018'
    # # 防止修改错误, 完成修改之后保存到其他文件夹当中，最后删除原来文件夹，复制到文件夹下（该操作建议手动）
    # save_gt_path = r'F:\dataset\Dehazy\I_HAZY_NTIRE_2018\cache\GT'
    # save_hazy_path = r'F:\dataset\Dehazy\I_HAZY_NTIRE_2018\cache\hazy'
    target_path = r'F:\dataset\Dehazy\O_HAZY_NTIRE_2018'
    # 防止修改错误, 完成修改之后保存到其他文件夹当中，最后删除原来文件夹，复制到文件夹下（该操作建议手动）
    save_gt_path = r'F:\dataset\Dehazy\O_HAZY_NTIRE_2018\cache\GT'
    save_hazy_path = r'F:\dataset\Dehazy\O_HAZY_NTIRE_2018\cache\hazy'
    target_gt_path = os.path.join(target_path, 'GT')
    target_hazy_path = os.path.join(target_path, 'hazy')
    
    # os.makedirs(save_gt_path, exist_ok=True)
    # os.makedirs(save_hazy_path, exist_ok=True)
    multi_makedirs(save_gt_path, save_hazy_path)

    batch_process_I_HAZY_NTIRE_2018(target_gt_path, save_gt_path,
                                    start_index=start_index, file_ext=file_ext, preview=preview)
    batch_process_I_HAZY_NTIRE_2018(target_hazy_path, save_hazy_path,
                                    start_index=start_index,file_ext=file_ext,preview=preview)