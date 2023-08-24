import csv
def read_csv_file(file_path):
    data = []
    # 打开指定路径的CSV文件，以只读模式
    with open(file_path, 'r') as f:
        reader = csv.reader(f) # 遍历
        for row in reader:
            data.append(row)
    return data  # 返回存储了CSV文件数据的列表
file_path = 'C:/Users/Cyan_wind/Downloads/fyx_chinamoney.csv'
data = read_csv_file(file_path)

code_list = data
#设置批大小为80
batch_size = 80

#开始分批
split_list = []
for i in range(0, len(code_list), batch_size):
    split_list.append(code_list[i:i+batch_size])

for i, batch in enumerate(split_list):
    print(f"Batch {i+1}: {batch}")