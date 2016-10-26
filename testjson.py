import json

# 用json文件保存配置项
def writeJson():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)
    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(json_str, f)

#读json文件的配置项
def readJson():
    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)
    datadic = eval(data)
    print(datadic['name'])



if __name__ == '__main__':
    writeJson()
    readJson()

'''
    # 一个Python数据结构转换为JSON
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)

    # 一个JSON编码的字符串转换回一个Python数据结构
    data = json.loads(json_str)

    #操作json文件
    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)
    '''
