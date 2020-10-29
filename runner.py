from mail import email_sender
from price_scrapper import price_scrapper_v1
from data_saver import data_saver
import matplotlib.pyplot as plt
from threading import Thread
import datetime
import time
import argparse

class runner:
	def __init__(self,url,username,password,target):
		self.url = url
		self.saver = data_saver()
		self.username  = username
		self.password = password
		self.target = target
		self.graph_image = f'graph{time.time()}.png'
		self.date = datetime.datetime.now().strftime('%d/%m/%y')

	def save_line_graph(self,list_of_costs):
		print('creating graph of the cost data collected')
		rates = list_of_costs
		days = range(1,len(rates)+1)
		plt.plot(days, rates, color='g')
		plt.xlabel('Time in DAYS ')
		plt.ylabel('Rate')
		plt.title('Line graph of product cost over Time')
		plt.savefig(self.graph_image)
		print('\n')

	def price_extractor_rec(self):
		for i in range(50) :
			is_succes,value = price_scrapper_v1(self.url)
			if not is_succes :
				# is_succes = false
				if value == 'out of stock':
					# send error email
					cost = 0
					return_value = False
					break

				elif value == 'not working properly':
					continue

			elif is_succes :
				# is_succes = True
				cost = int(value)
				return_value = True
				break

		else :
			# request not working for 20 time !!!
			return_value = False
			cost = 0

		return return_value,cost

	def error_mail(self):
		print(f'sending error message to the target {self.target}')
		email_contents = {'subject':'Error in tracking product cost with Python'}
		email_contents['product_url'] = self.saver.template['product_url']
		email_contents['product_cost'] = self.saver.read_data()['costs'][-1]
		email_contents['higest_cost'] = self.saver.template['max_cost']
		email_contents['lowest_cost'] = self.saver.template['min_cost']
		email_sender.error_message_occasion(self.username,self.password,self.target,email_contents)
		raise Exception('Error in executing the code for this url !!')

	def first_time_only(self):
		'''
		1. request for price
		2. create json file with url and price
		3. send email
		'''
		# extracting the value of price
		return_value,cost =	self.price_extractor_rec()
		
		# save json file
		print('saveing results in json file')
		self.saver.create_template(self.url,cost)

		# send mail##############
		print(f'sending email to the given target {self.target}')
		email_contents = {'subject':'Stating tracking product cost with Python'}
		email_contents['product_url'] = self.saver.template['product_url']
		email_contents['product_cost'] = self.saver.read_data()['costs'][-1]
		
		# send starting mail
		email_sender.first_message_once(self.username,self.password,self.target,email_contents)
		
		if not return_value :
			# send starting and error mail#######
			self.error_mail()

	def daily(self):
		'''
		it may be run x time in a day
		check for change in rates if present then send mail

		'''
		# ectracting cost from site 
		return_value,cost = self.price_extractor_rec()
		# print(return_value,cost)
		# if return_value = true then 
		if return_value :
			# update cost of today in the json file if already not done
			date = datetime.datetime.now().strftime('%d/%m/%y')
			if self.date != date :  
				self.saver.update_a_field('costs',cost)
				self.date = date 

			# if cost of the product is change then send mail
			if self.saver.read_data()['costs'][-1] != cost :
				# send mail 
				print(f'sending message to the target {self.target} of cost update')
				email_contents = {'subject':'Product cost changed !!'}
				email_contents['product_url'] = self.saver.template['product_url']
				email_contents['new_cost'] = cost
				email_contents['higest_cost'] = self.saver.template['max_cost']
				email_contents['lowest_cost'] = self.saver.template['min_cost']
				email_sender.cost_updating_weekly(self.username,self.password,self.target,email_contents)
				# self.saver.update_a_field('costs',cost)
	
		
		elif not return_value :
			# if there is any problem in extracting the cost
			self.error_mail()

	def weekly_mail(self):
		'''
		send mail to target weekly update with attached
		1. graph 
		2. price.data.json file'''

		# create graph from the cost data		
		self.save_line_graph(self.saver.read_data()['costs'])

		# sending mail
		email_contents = {'subject':'Product cost weekly update'}
		email_contents['product_url'] = self.saver.template['product_url']
		email_contents['new_cost'] = self.saver.read_data()['costs'][-1]
		email_contents['higest_cost'] = self.saver.template['max_cost']
		email_contents['lowest_cost'] = self.saver.template['min_cost']
		email_sender.cost_updating_weekly(self.username,self.password,self.target,email_contents,attachment=True,filename=[self.graph_image,self.saver.file_name])

	@staticmethod
	def intro():
		# print the brief intro of the program
		print("This program will track a product cost of the given url \nand send emails updates to the target's email by given email and password \n\nupdates are :-\n1.starting (once only) \n2.weekly (every week with graphical representaion)\n3.Instantaneous (If the cost change)\n")

	@classmethod
	def runner(cls,url,username,password,target):
		# this funtion will run for max 6 month
		run = cls(url,username,password,target)
		run.first_time_only()

		# 6 months/weeks = 4*6 = 24
		for week in range(24):
			print('running week =>',week)
			for i in range(1,8):
				for j in range(1,3) :  # twice a day
					print(f'\tday {i}.{j}')
					Thread(target = run.daily())
					print('\twent to sleep for 12h')
					time.sleep(12*60*60) # half day sleep here = 60*60*12


			else :
				print('sending week-end computation mail of all the data collected')
				Thread(target = run.weekly_mail() )
				print('\n\n')


if __name__ == '__main__':
	# url = 'https://www.amazon.in/pibox-India-Raspberry-Broadcom-Processor/dp/B07XSJH3C5/ref=sr_1_1?crid=14QXN8HX02OZZ&dchild=1&keywords=resbary+pie+4&qid=1603605694&sprefix=resb%2Caps%2C401&sr=8-1'
	# runner.runner(url,username,password,target)
	parser = argparse.ArgumentParser()
	parser.add_argument('--intro',action="store_true",help = "give brief intro of the program")
	parser.add_argument('-u','--url' ,help = "url of the product to track")
	parser.add_argument('-a','--user' ,help = "user-email-address@gmail.com")
	parser.add_argument('-p','--password' ,help = "password of the user-email-address@gmail.com")
	parser.add_argument('-t','--target' ,help = "target email address")
	# if file is given then we need only file data nothing more
	parser.add_argument('-f','--file' ,help ="file name if data is saved into file")

	args = parser.parse_args()
	if args.intro :
		# give into of the funtion
		runner.intro()
		pass

	if args.file:
		# when data is given in the form of file
		print(f'Reading file for credentials in {args.file}')
		with open(args.file,'r') as file:
			lines = file.readlines()
			cleared_lines= [i.replace('\n','') for i in lines if i != '\n']
			values=dict()
			for line in cleared_lines :
				field,value = line.split('=',1)
				values[field.strip()]=value.strip()

		try :
			# confirm that all the values are recived
			if values['username'] and values['password'] and values['target'] and values['url'] :
				pass
		except :
			raise Exception('There is not enought varible for our requirement\nshould have:-\n1.username\n2.password\n3.target\n4.url')

		# calling the funtion here
		# print(f'\nInitiating the process by {args.file}')
		runner.runner(values['url'],values['username'],values['password'],values['target'])

	elif args.url and args.user and args.password and args.target :
		# when all the data is given in commend-line
		print('\nInitiating the process')
		# print(args.url,args.user,args.password,args.target)
		runner.runner(args.url,args.user,args.password,args.target)

