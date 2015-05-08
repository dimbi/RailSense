def binary(node):
	node['left'] = node
	node['right'] = node['left']

dic = {}

dic['left'] = binary(dic)
dic['right'] = dic['left']

print dic