import pickle
import traceback
from scipy.sparse import csr_matrix
def load_pkl_file(file_path):
    try:
        # 打开并加载 .pkl 文件
        with open(file_path, 'rb') as file:
            data = pickle.load(file)

        # 打印加载的数据类型
        print(f"Loaded data type: {type(data)}")

        # 如果是字典，打印键
        if isinstance(data, dict):
            print("Keys in the dictionary:")
            for key in data.keys():
                print(key)

        # 如果是列表或其他类型，打印数据内容
        else:
            print("Data content:")
            print(data)

        return data
    except ModuleNotFoundError as e:
        print(f"Error: {e}")
        print("It seems you are missing a required module. Please install the necessary module and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(traceback.format_exc())

# 使用示例：提供 .pkl 文件的路径
# file_path = 'Datasets/Yelp/trn_tip'  # 将 'your_file.pkl' 替换为你的 .pkl 文件路径
file_path = 'Datasets/lkx/offered'  # 将 'your_file.pkl' 替换为你的 .pkl 文件路径
data = load_pkl_file(file_path)
