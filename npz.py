
import numpy as np

def load_npz_file(file_path):
    # 使用 np.load 读取 .npz 文件
    with np.load(file_path) as data:
        # 打印文件中所有数组的名称
        print("Arrays in the .npz file:")
        for array_name in data.files:
            print(array_name)
            # 获取对应的数组
            array = data[array_name]
            print(f"Array '{array_name}' has shape {array.shape} and dtype {array.dtype}")
            # 打印数组内容（根据需要可以注释掉）
            print(array)
            print()

file_path = 'Datasets/Yelp/offered.npz'  #
load_npz_file(file_path)
