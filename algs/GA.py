#遗传算法学习
#计算f(x) = x+ 10 *sin(5*x)+7*cos(4x)在[0,9]
import math
import random
import matplotlib.pyplot as plt
class GA():
	#初始化种群
	#参数n位种群数目，默认为30
	#设置交叉率，默认位0.6
	#设置变异率，默认为0.01
	def __init__(self, n = 30, cross_rate = 0.85, mutation_rate = 0.05):
		#假设求解精确到小数，点后4位，则有9000个解
		#选择编码位位17
		#种群个数在n-2n，选择30
		self.genu_len = 17
		self.genu_num = n
		self.max_value = 9.0
		self.min_value = 0.0
		self.max_fitness = -26
		self.max_x = 0.0
		self.cross_position = 7
		self.cross_rate = cross_rate
		self.mutation_rate = mutation_rate
		self.scale = (self.max_value - self.min_value)/(2**self.genu_len - 1)
		self.genu = []
		#产生随机数种子，方便调试
		for i in range(self.genu_num):
			data = random.uniform(self.min_value, self.max_value)
			self.genu.append(self.encode(data))

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

	#求值函数
	def calculate(self,vaule):
		return vaule + 10*math.sin(5*vaule) + 7*math.cos(4*vaule)

	#适应度函数
	def fitness(self):
		self.fit_problity = []
		min_fitness_value = 26
		for i in range(len(self.genu)):
			data_value = self.calculate(self.decode(self.genu[i]))
			self.fit_problity.append(data_value)
			if (data_value > self.max_fitness):
				self.max_fitness = data_value
				self.max_x = self.decode(self.genu[i])
			if (data_value < min_fitness_value):
				min_fitness_value = data_value
		# 如果最小值小于0，则进行平移

		if min_fitness_value < 0:
			for i in range(len(self.genu)):
				self.fit_problity[i] -= min_fitness_value

		#计算所有的和
		tmp_sum = 0
		for i in range(len(self.genu)):
			tmp_sum += self.fit_problity[i]
		
		for i in range(len(self.genu)):
			self.fit_problity[i] = self.fit_problity[i] / tmp_sum
			


	#选择
	def selection(self):
		#使用轮盘赌
		#首先产生一个0-1之间的数
		rand = random.random()
		problity_sum = 0.0
		for i in range(len(self.genu)):
			problity_sum += self.fit_problity[i]
			if(problity_sum) > rand:
				return self.genu[i]
		print("出现概率之和小于1")
		print("概率和：", problity_sum)
		return None

	#交叉
	def crossover(self, father, mother):
		#采用单点交叉运算，选择的交叉点为7
		rand = random.random()
		if rand < self.cross_rate:
			#进行交叉操作
			child_one = father[0:self.cross_position] + mother[self.cross_position:]
			child_two = mother[0:self.cross_position] + father[self.cross_position:]
		else:
			child_one = father
			child_two = mother
		return child_one,child_two

		

	#变异
	def mutation(self, data_string):
		rand = random.random()
		if rand < self.mutation_rate:
			#进行变异,随机产生变异位置
			position = math.floor(random.uniform(0,self.genu_len))
			#此处无法直接修改
			if data_string[position] == "0":
				data_string = data_string[0:position]+"1"+ data_string[position:]
			else:
				data_string = data_string[0:position]+"0"+ data_string[position:]
		return data_string

	def generate_new(self):
		new_genu = []
		self.fitness()
		for i in range (int(self.genu_num /2)):
			father = self.selection()
			mother = self.selection()
			child_one, child_two = self.crossover(father,mother)
			child_one = self.mutation(child_one)
			child_two = self.mutation(child_two)
			new_genu.append(child_one)
			new_genu.append(child_two)
		self.genu = new_genu

if __name__ == "__main__":
	print("开始执行程序：")
	ga = GA(n = 30, cross_rate = 0.85, mutation_rate = 0.2)
	#ga = GA()
	# 测试encode 和 decode
	i = 0
	num = []
	value = []
	while i < 100:
		print("迭代次数：",i)
		ga.generate_new()
		print("染色体个数:",len(ga.genu))
		print (ga.max_fitness)
		print(ga.max_x)
		num.append(i)
		value.append(ga.max_fitness)
		i = i + 1

	plt.plot(num,value)
	plt.show()