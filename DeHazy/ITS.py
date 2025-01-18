# ITS (Indoor Training Set)
# 下载的时候文件夹名为 ITS_v2
""" https://github.com/Auorui/img-processing-techniques
ITS_v2
    - clear
    - hazy
请注意,在去雾当中我个人习惯使用png格式的图片,如果要保留原来格式的,请注意修改格式是否正确
hazy: 1_1_0.90179.png -----> 1_1.png

clear 是按照我们的目标格式来的
"""
# 先修改 ./ITS_v2/hazy下文件的命名格式, 直接在原有基础上修改
import os
from pathlib import Path
from natsort import natsorted
import shutil
from utils import multi_makedirs
from math import ceil
import random

def SearchFileName(target_path, file_ext='.png'):
    """该函数将会放入在
    https://github.com/Auorui/img-processing-techniques
    下的 utils 文件夹当中, 以后将会多次使用
    仅仅搜索目标文件夹下合适格式的文件名
    """
    all_files = os.listdir(target_path)
    png_files = [file for file in all_files if file.lower().endswith(file_ext)]
    sorted_png_files = natsorted(png_files)
    return sorted_png_files

def batch_process_ITS_v2_hazy(
    target_path,
    file_ext=None,
    preview=True,
):
    file_name_list = SearchFileName(target_path)
    nums_file = len(file_name_list)
    for i in range(nums_file):
        file_extension = Path(file_name_list[i]).suffix if file_ext is None else file_ext
        # 1399_8_0.74031  ----->  1399_8
        file_name_no_suffix = os.path.splitext(file_name_list[i])[0].split('_')
        new_name = file_name_no_suffix[0] + "_" + file_name_no_suffix[1]
        new_file_name = f"{new_name}{file_extension}"
        old_file_path=os.path.join(target_path, file_name_list[i])
        new_file_path=os.path.join(target_path, new_file_name)
        if not preview:
            os.rename(old_file_path, new_file_path)
        print(f"Renamed: {file_name_list[i]} -> {new_file_name}")


def divide_ITS_v2_dataset(
    target_path,
    save_path,
    train_ratio,
    val_ratio,
    shuffle=True,
    preview=True,
) :
    original_gt_path = os.path.join(target_path, 'clear')
    original_hazy_path = os.path.join(target_path, 'hazy')

    save_train_path = os.path.join(save_path, "train")
    save_val_path = os.path.join(save_path, "val")
    save_test_path = os.path.join(save_path, "test")

    train_txt_path = os.path.join(save_path, "train.txt")
    val_txt_path = os.path.join(save_path, "val.txt")
    test_txt_path = os.path.join(save_path, "test.txt")

    multi_makedirs(os.path.join(save_train_path, "GT"), os.path.join(save_train_path, 'hazy'),
                   os.path.join(save_val_path, "GT"), os.path.join(save_val_path, 'hazy'),
                   os.path.join(save_test_path, "GT"), os.path.join(save_test_path, 'hazy'),)

    file_name_list = SearchFileName(original_gt_path)
    if shuffle:
        random.shuffle(file_name_list)

    nums_file = len(file_name_list)

    train_nums = ceil(nums_file * train_ratio)
    if train_ratio + val_ratio == 1.:
        val_nums = nums_file - train_nums
        test_nums = 0
    else:
        val_nums = ceil(nums_file * val_ratio)
        test_nums = nums_file-(train_nums+val_nums)

    print(f"划分数据集数量, 总数{nums_file}, train:{train_nums}, test:{val_nums}, test:{test_nums}")
    total = total1 = total2 = 1
    for i in range(train_nums):
        image_gt_name = file_name_list[i]
        image_hazy_name = f"{image_gt_name.split('.')[0]}_{random.randint(1, 10)}.{image_gt_name.split('.')[1]}"

        a_gt_path = os.path.join(original_gt_path, image_gt_name)
        a_hazy_path = os.path.join(original_hazy_path, image_hazy_name)
        save_new_path_gt = os.path.join(save_train_path, "GT", image_gt_name)
        save_new_path_hazy = os.path.join(save_train_path, "hazy", image_gt_name)

        if not preview:
            shutil.copy(a_gt_path, save_new_path_gt)
            shutil.copy(a_hazy_path, save_new_path_hazy)

            with open(train_txt_path, 'a') as train_txt_file:
                train_txt_file.write(image_gt_name.split('.')[0] +'\n')

        print(f"{total} train: {i + 1}\n"
              f"{a_gt_path} ----> {save_new_path_gt}\n"
              f"{a_hazy_path} ----> {save_new_path_hazy}")
        total += 1

    for i in range(train_nums, nums_file):
        if i < train_nums + val_nums:
            image_gt_name = file_name_list[i]
            image_hazy_name = f"{image_gt_name.split('.')[0]}_{random.randint(1,10)}.{image_gt_name.split('.')[1]}"
            a_gt_path = os.path.join(original_gt_path,image_gt_name)
            a_hazy_path = os.path.join(original_hazy_path,image_hazy_name)
            save_new_path_gt = os.path.join(save_train_path,"GT",image_gt_name)
            save_new_path_hazy = os.path.join(save_train_path,"hazy",image_gt_name)
            if not preview:
                shutil.copy(a_gt_path, save_new_path_gt)
                shutil.copy(a_hazy_path, save_new_path_hazy)

                with open(val_txt_path, 'a') as val_txt_file :
                    val_txt_file.write(image_gt_name.split('.')[0]+'\n')
            print(f"{total} val: {i+1}\n"
                  f"{a_gt_path} ----> {save_new_path_gt}\n"
                  f"{a_hazy_path} ----> {save_new_path_hazy}")
            total1 += 1
        else:
            image_gt_name = file_name_list[i]
            image_hazy_name = f"{image_gt_name.split('.')[0]}_{random.randint(1,10)}.{image_gt_name.split('.')[1]}"
            a_gt_path = os.path.join(original_gt_path,image_gt_name)
            a_hazy_path = os.path.join(original_hazy_path,image_hazy_name)
            save_new_path_gt = os.path.join(save_train_path,"GT",image_gt_name)
            save_new_path_hazy = os.path.join(save_train_path,"hazy",image_gt_name)
            if not preview:
                shutil.copy(a_gt_path, save_new_path_gt)
                shutil.copy(a_hazy_path, save_new_path_hazy)

                with open(test_txt_path, 'a') as test_txt_file :
                    test_txt_file.write(image_gt_name.split('.')[0]+'\n')
            print(f"{total2} test: {i+1}\n"
                  f"{a_gt_path} ----> {save_new_path_gt}\n"
                  f"{a_hazy_path} ----> {save_new_path_hazy}")
            total2 += 1


if __name__=="__main__":

    def rename_ITS_v2_hazy() :
        # 建议先进行预览 True, 避免出错, 确定没问题后改为False
        preview=True
        # 目标文件夹路径
        original_hazy_path=r'F:\dataset\Dehazy\ITS_v2\hazy'
        # 后缀名, 如果为None, 就使用原来的后缀
        file_ext='.png'
        batch_process_ITS_v2_hazy(original_hazy_path,file_ext,preview)

    # 先运行这个代码, 完了之后注释掉, 再运行下面代码, 参数直接在函数内部修改
    # rename_ITS_v2_hazy()

    # 建议先进行预览 True, 避免出错, 确定没问题后改为False
    preview = False
    # 训练集比例
    train_ratio = 0.7
    # 验证集比例，剩下的就是测试集比例，如果train_ratio + val_ratio = 1. ,则不划分测试集
    val_ratio = 0.2
    # 是否打乱数据集划分顺序
    shuffle = True
    original_path = r'F:\dataset\Dehazy\ITS_v2'
    save_path = r'F:\dataset\Dehazy\ITS_v2\cache'
    divide_ITS_v2_dataset(original_path, save_path, train_ratio, val_ratio,
                          shuffle=shuffle, preview=preview)


