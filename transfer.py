import numpy as np
import pickle


def npz_to_pickle(npz_file_path, pkl_file_path):
    # 加载 .npz 文件
    with np.load(npz_file_path) as data:
        # 将数据转换为字典格式
        data_dict = {file: data[file] for file in data.files}

    # 使用 pickle 保存为 .pkl 文件
    with open(pkl_file_path, 'wb') as pkl_file:
        pickle.dump(data_dict, pkl_file)

    print(f"Data has been successfully converted from {npz_file_path} to {pkl_file_path}")


# 调用函数，提供 .npz 文件路径和输出的 .pkl 文件路径
npz_file_path = 'Datasets/lkx/test_data_sold.npz'  # 将 'your_file.npz' 替换为你的 .npz 文件路径
pkl_file_path = 'Datasets/lkx/test_data_sold'  # 将 'output_file.pkl' 替换为你想要保存的 .pkl 文件路径

npz_to_pickle(npz_file_path, pkl_file_path)
