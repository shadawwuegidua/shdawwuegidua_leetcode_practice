# 字典的基本操作

student = {"name": "小明", "age": 18, "score": 90, 60:70}  # 键值对结构
print(student["name"])  # 输出 "小明"（通过key访问value）
student["age"] = 19     # 修改value，age 变成 19
student["gender"] = "男"# 添加新键值对
del student["score"]    # 删除键值对
print(student[60])
print(id)
print(print)
print(hex(id(student)))
print(bin(id(student)))
for key in student.keys():
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print((key, value))
print(student)          # 输出 {'name': '小明', 'age': 19, 'gender': '男'}
nums = [1,2,4,5,6]
del nums[3]
print(nums)

# --- 验证你的问题 ---

# 1. 字典的 [i] 是指 Key 也就是键，而不是第 i 个位置
test_dict = {0: "a", 10: "b", 2: "c"}
# print(test_dict[1])  # 这会报错 KeyError，因为没有 key 叫 1，虽然它是第二个元素
print(test_dict[10])   # 输出 "b"，因为有一个 key 叫 10

# 2. 字典的顺序
# 在 Python 3.7+ 中，字典保持"插入顺序"
order_dict = {}
order_dict['first'] = 1
order_dict['second'] = 2
order_dict['third'] = 3
print(order_dict) # 输出顺序一定是你添加的顺序：first, second, third

# 3. 字典的排序
# 字典本身不支持 .sort() 原地排序，但可以用 sorted() 生成一个排序后的列表或新字典
scores = {'C': 80, 'A': 95, 'B': 88}

# 按 Key 排序
sorted_by_key = dict(sorted(scores.items())) 
print("按Key排序:", sorted_by_key) # {'A': 95, 'B': 88, 'C': 80}

# 按 Value 排序
sorted_by_value = dict(sorted(scores.items(), key=lambda item: item[1]))
print("按Value排序:", sorted_by_value) # {'C': 80, 'B': 88, 'A': 95}
# help(print)
# help(dict)
