import json
import datetime
# createing a json file and save the results

class data_saver:
	def __init__(self):
		self.template ={
			'product_url':'',
			'initial_date':'',
			'costs':[],
			'min_cost':0,
			'max_cost':0
		}
		self.file_name ='price_data.json' 

	def create_template(self,url,cost):
		self.template['product_url'] = url
		self.template['initial_date'] = datetime.datetime.now().strftime('%d/%m/%y')
		self.template['costs'].append(cost)
		self.template['min_cost'] = cost
		self.template['max_cost'] = cost
		with open(self.file_name ,'w') as json_file:
			json.dump(self.template,json_file,indent=4)

	def read_data(self):
		with open(self.file_name,'r') as json_file :
			return json.load(json_file)

	def save_data(self,new_data):
		with open(self.file_name,'w') as json_file :
			json.dump(new_data,json_file,indent=4)

	def update_a_field(self,field,value):
		data = self.read_data()
		if field != 'costs' : data[field] = value
		else :
			data[field].append(value)
			if self.template['min_cost'] > value:
				self.template['min_cost'] = value
				data['min_cost'] = value
			if self.template['max_cost'] < value :
				self.template['max_cost'] = value 
				data['max_cost'] = value

		self.save_data(data)



if __name__ == '__main__':
	a = data_saver()
	a.create_template('www.google.com',100)
	# # a.save_data()
	# print(a.read_data())
	a.update_a_field('costs',100)
	a.update_a_field('costs',10000)
