#遗传算法学习
#计算f(x) = x+ 10 *sin(5*x)+7*cos(4x)在[0,9]
import math
class GA():
	#初始化种群
	#参数n位种群数目，默认为30
	def __init__(self, n = 30):
		#假设求解精确到小数，点后4位，则有9000个解
		#选择编码位位17
		#种群个数在n-2n，选择30
		self.genu_len = 17
		self.max_value = 9.0
		self.min_value = 0.0
		self.scale = (self.max_value - self.min_value)/(2**self.genu_len - 1)

	#编码函数
	#输入一个浮点数，返回一个字符串
	def encode(self, data):
		num = math.floor(data / self.scale)
		result =  "{0:b}".format(num)
		zero_need_add = self.genu_len - len(result)
		if(zero_need_add > 0):
			tmp = ""
			for i in range(zero_need_add):
				tmp += "0"
			result += tmp
		return result


	#解码函数
	#输入一个字符串，返回一个浮点数
	def decode(self, bin_string):
		data = 0
		for i in range(self.genu_len):
			if(bin_string[i] == '1'):
				data += 2**(self.genu_len - 1 - i)
		
		return data * self.scale

	#适应度函数
	def fitness(self):
		pass

	#选择
	def slection(self):
		pass

	#交叉
	def crossover(self):
		pass

	#变异
	def mutation(self):
		pass

if __name__ == "__main__":
	print("开始执行程序：")
	ga = GA()
	# 测试encode 和 decode
	data = 6
	data_string = ga.encode(data)
	print(data_string)
	print(ga.decode(data_string))
