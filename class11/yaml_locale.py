import yaml
'''
    yaml文件读取文件与常规的文件不同,通过open形成file格式的内容,给予yaml库实现内容的识别和读取

'''

file = open('./data/data.yaml','r',encoding='utf-8')
# 读取yaml格式的数据内容并保存原有格式
data = yaml.load(stream=file,Loader=yaml.FullLoader)
print(type(data))
print(data)








