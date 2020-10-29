import smtplib
from email.message import EmailMessage
import os
import datetime

class messages :
    def cost_update(new_cost,higest_cost,lowest_cost,product_url):
        ''' return html from the given values '''
        date = datetime.datetime.now().strftime('%d/%m/%y')
        profit = (higest_cost - new_cost) if (higest_cost - new_cost) > 0 else 0 
        mess = f'''
            <body style="background: #F4F4F4;">
            <div style="background-color: #000000; text-align: center;font-size: 25px; margin: 0px;">
                <h1 style="color: white;">Cost Update</h1>
            </div>
            <!-- completed -->
            <div style="font-weight: bolder;">
                <div style="padding-left: 1em;padding-right: 1em;font-size: 25px;height: 5vh; ">
                    <div style="float: left;">Date: <span style="font-weight: 200;">  {date}</span></div>
                    <div style="float: right; background: rgba(36, 84, 255, 0.8);border-radius: 10px; padding: 5px;box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.5);">
                        <a href="{product_url}" style="text-decoration: none;color: white;font-weight: bold;">Product Url</a>
                    </div>
                </div>
                <!-- completed -->

                <div style="font-size: 30px;height: 15vh; padding: 2em;">
                    <div style=" text-align: center;margin: auto;">New Cost : <span style="font-weight: 200;font-size: 25px;"> ₹{new_cost}</span> </div>
                    <div style=" text-align: center;margin: auto;">Profit : <span style="font-weight: 200;font-size: 25px;"> ₹{profit}</span> </div>
                </div>

                <div style="font-size: 30px;">
                    <div style="float: left;">Higest cost :<span style="font-weight: 200;font-size: 25px;">₹{higest_cost}</span> </div>
                    <div style="float: right;">Lowest cost :<span style="font-weight: 200;font-size: 25px;">₹{lowest_cost}</span> </div>
                </div>
            </div>
        </body>
        '''
        return mess 

    def error(higest_cost,lowest_cost,product_url):
        ''' return the errer html '''
        date = datetime.datetime.now().strftime('%d/%m/%y')
        mess = f'''
        <body style="background: #F4F4F4;">
            <div style="background-color:  rgba(255, 0, 0, 0.47); text-align: center;font-size: 25px; margin: 0px;">
                <h1>Cost Update Error</h1>
            </div>
            <!-- completed -->
            <div style="font-weight: bolder;">
                <div style="padding-left: 1em;padding-right: 1em;font-size: 35px;height: 5vh; ">
                    <div style="float: left;">Date: <span style="font-weight: 200;">{date}</span></div>
                    <div style="float: right; background: rgba(36, 84, 255, 0.8);border-radius: 10px; padding: 5px;box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.5);">
                        <a href="{product_url}" style="text-decoration: none;color: white;font-weight: bold;">Product Url</a>
                    </div>
                </div>
                <!-- completed -->

                <div style="margin: 2px;font-size: 35px;">
                    <h1 style="font-size: 50px;text-align: center;color: #DC2D2D;">ERROR !!!</h1>
                    <div class="list" style="align-self: center; width: 50vw;margin: auto;  ">
                        <h3 style="font-weight: bolder;font-size: 35px;">Possible error :- </h3>
                        <ol style="padding-left: 1em;">
                            <li style=" font-weight:400; ">
                                Url not found.
                            </li>
                            <li style="font-weight:400; ">
                                Unable to extract price from its page.
                            </li>
                            <li style="font-weight:400; ">
                                Item is not in stock.
                            </li>
                        </ol>
                    </div>
                </div>

                <div style="font-size: 30px; ">
                    <div style="float: left; ">Higest cost :<span style="font-weight: 200;font-size: 25px; ">₹{higest_cost}</span> </div>
                    <div style="float: right; ">Lowest cost :<span style="font-weight: 200;font-size: 25px; ">₹{lowest_cost}</span> </div>
                </div>
            </div>
        </body>
        '''
        return mess
        
    def stating(product_cost,product_url):
        date = datetime.datetime.now().strftime('%d/%m/%y')
        mess = f'''
        <body style="background: #F4F4F4;">
            <div style="background-color: rgba(0, 0, 0, 0.5);color:white; text-align: center;font-size: 20px; margin: 0px;">
                <h1>Starting Email Notifications</h1>
            </div>
            <!-- completed -->
            <div style="font-weight: bolder;">
                <div style=" padding-left: 1em;padding-right: 1em;font-size: 25px;">
                    <div>Date: <span style="font-weight: 200;"> {date}</span></div>
                    <div style="margin: 2em auto; width: fit-content; padding: 5px;  text-align: center; background: rgba(36, 84, 255, 0.8);border-radius: 10px; box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.5);">
                        <a href="{product_url}" style="text-decoration: none;font-size: 35px;color: white;font-weight: bold;">Product Url</a>
                    </div>
                </div>
                <!-- completed -->

                <div style="padding: 1em;margin: 2px;">
                    <h1 style="text-align: center;">Product cost :<span style="font-weight: 200;">₹{product_cost}</span></h1>
                </div>


            </div>
        </body>
        '''
        return mess

# print(messages.stating(0,'#'))

class email_sender:
	# creating html-message 
	def __init__(self,username,password,target):
		self.username = username
		self.password = password
		self.message = EmailMessage()
		self.message['from'] = username
		self.message['to'] = target

	def add_message(self,subject,body):
		''' take subject and body and add given message to the message package '''
		# subject body 
		self.message['Subject'] = subject
		# set content of the body in html format
		self.message.add_alternative(body,subtype = 'html')
		print('Email suject and body are attached ')

	def add_attachments(self,filename = None,directory = None):
		# adding files in here ######### unable to find any docs to attaching py files
		if filename != None:
			files = [*filename]    # now we can add multiple files here in the form of list or tuple -> 'a' or ['a','b'] or ('a','b') 
		elif directory != None:
			files = os.listdir(directory)
		else :
			print('There is nothing to connect with mail')
			return

		for i,file in enumerate(files):
			print('{}. adding {}'.format(i+1, file))
			if file == '__pycache__':
				continue
			with open(file,'rb') as file:
				file_data = file.read()  # return some bytes
				name = file.name	 # return name of file ex 1.png
				extension = name.split('.')[-1]   # extracting extention of file/file
				if extension in ['jpg','JPG','png','PNG','ico','jpg2']:
					# when file is image
					self.message.add_attachment(file_data,maintype='image',subtype=extension,filename=name)
				elif extension in ['pdf','PDF']:
					# if file is pdf
					self.message.add_attachment(file_data,maintype='application',subtype='octet-straem',filename=name)
				else : 
					# any thing else which is txt
					self.message.add_attachment(file_data,maintype='text',subtype='txt',filename=name)

	def executor(self,subject,body,attachment =	False,**kwargs):
		# this executor is specific for my use for this program can be update for more viscosity in program
		with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp :
			smtp.login(self.username,self.password)  # login
			self.add_message(subject,body)
			
			if attachment:
				try :
					if  kwargs['filename']:
						self.add_attachments(filename=kwargs['filename'])   # adding attachments
				except:
					if kwargs['directory']:
						self.add_attachments(directory=kwargs['directory'])   # adding attachments

			smtp.send_message(self.message)  #sending mail
			print('Mail is send\n')


	@classmethod
	def first_message_once(cls,username,password,target,email_contents,**kwargs):
		# email_contents= ['Subject',(values for the messages=)suject,product_cost,product_url]
		mail = cls(username,password,target)
		mail.executor(email_contents['subject'],messages.stating(email_contents['product_cost'],email_contents['product_url']),**kwargs)

	@classmethod
	def error_message_occasion(cls,username,password,target,email_contents,**kwargs):
		# email_contents= ['Subject',(values for the messages=)suject,higest_cost,lowest_cost,product_url)]
		mail = cls(username,password,target)
		mail.executor(email_contents['subject'],messages.error(email_contents['higest_cost'],email_contents['lowest_cost'],email_contents['product_url']),**kwargs)

	@classmethod
	def cost_updating_weekly(cls,username,password,target,email_contents,**kwargs):
		# email_contents= ['Subject',(values for the messages=)subject, new_cost,higest_cost,lowest_cost,product_url]
		mail = cls(username,password,target)
		# cost_update(new_cost,higest_cost,lowest_cost,product_url
		mail.executor(email_contents['subject'],messages.cost_update(email_contents['new_cost'],email_contents['higest_cost'],email_contents['lowest_cost'],email_contents['product_url']),**kwargs)




if __name__ == '__main__':
	# from seckret import *	
	email_contents= {'subject':132,
	'product_cost':5298,
	'new_cost':5298,
	'higest_cost':5500,
	'lowest_cost':5000,
	'product_url':'https://www.youtube.com/watch?v=Jllu94-8PxI&list=RDMM98WtmW-lfeE&index=27'}
	email_sender.first_message_once(username,password,target,email_contents)
	email_sender.cost_updating_weekly(username,password,target,email_contents,attachment=True,filename=['intro.txt','price_data.json'])
	email_sender.error_message_occasion(username,password,target,email_contents)

