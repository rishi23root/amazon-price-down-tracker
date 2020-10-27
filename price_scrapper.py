from bs4 import BeautifulSoup
import requests

def price_scrapper_v0(url):
	# use of headers sometimes don't give good results may session work good here
	headers = {
	    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
		}

	r = requests.get(url,headers = headers)
	if r.status_code == requests.codes.ok :
		soup = BeautifulSoup(r.content, "html.parser")
		try :
			# Currently unavailable.
			ele = soup.find(id='availability',class_= "a-section a-spacing-none").find('span')
			# print(ele.text.strip())
			if ele.text.strip() == "Currently unavailable.":
				# if currently_una != None :b
				print('out of stock')
				return (False, 'out of stock')
		except :
			pass

		try :
			price = soup.find(id="priceblock_saleprice", class_="a-size-medium a-color-price priceBlockSalePriceString").get_text()
			price =	price.split('₹ ')[-1].split('.')[0].replace(',','')	
			return (True,price)
		except :
			print('not working properly')
			return (False,'not working properly')
	else :
		print(r.status_code)


def price_scrapper_v1(url):
	# vesion can extract all type of price just not kindle book may update in further version
	headers = {
	    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
		}

	with requests.Session() as s:
		s.get('https://www.amazon.in/',headers = headers)
		r = s.get(url,headers = headers)

	# r = requests.get(url,headers = headers)
	if r.status_code == requests.codes.ok :
		soup = BeautifulSoup(r.content, "html.parser")
		try :
			# Currently unavailable.
			ele = soup.find(id='availability',class_= "a-section a-spacing-none").find('span')
			# print(ele.text.strip())
			if ele.text.strip() == "Currently unavailable.":
				print('out of stock')
				return (False, 'out of stock')
		except :
			pass

		try :
			price = soup.find(id="priceblock_saleprice", class_="a-size-medium a-color-price priceBlockSalePriceString")
			if price == None:
				price = soup.find(id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
			if price == None:
				price = soup.find(id="priceblock_dealprice", class_ ="a-size-medium a-color-price priceBlockDealPriceString")
			price=price.get_text()
			price =	price.split('₹ ')[-1].split('.')[0].replace(',','')	
			return (True,price)
		except :
			print('not working properly')
			return (False,'not working properly')
	else :
		print(r.status_code)
		return (False,'wrong status_code')



if __name__ == '__main__':
	print(price_scrapper_v1(url='https://www.amazon.in/New-Apple-iPhone-12-64GB/dp/B08L5T3S7T/ref=sr_1_3?dchild=1&keywords=iphone+12&qid=1603675493&sr=8-3'))
	print(price_scrapper_v1(url='https://www.amazon.in/Introducing-Echo-Show-8-display-screen/dp/B07SMNPCGK/ref=lp_20871486031_1_1?s=amazon-devices&ie=UTF8&qid=1603674918&sr=1-1'))
	print(price_scrapper_v1(url='https://www.amazon.in/Sony-WF-XB700-Wireless-Bluetooth-Headphones/dp/B085VQFZ8Z/ref=sr_1_1_sspa?_encoding=UTF8&dchild=1&m=A14CZOWI0VEHLG&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=01f5e5a4-6b2b-448a-ba8a-9e2e2f6daab8&pf_rd_r=DF3WR6PQMNNXPEBMS1TX&pf_rd_t=36701&qid=1603042268&refinements=p_89%3ABLAUPUNKT%7CBlaupunkt%7CEnvent%7CModernista%7CPHILIPS%7CSony%7CTHOMSON%7CZoook%2Cp_6%3AA14CZOWI0VEHLG&rnid=1318474031&s=electronics&smid=A14CZOWI0VEHLG&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVFJaSjVSV1dCVkU5JmVuY3J5cHRlZElkPUEwNTI0MzcyOUlWS1VFS0FaMVczJmVuY3J5cHRlZEFkSWQ9QTA3OTA5OTkzVjRLNUFHSlFVTTdJJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='))
	print(price_scrapper_v1(url='https://www.amazon.in/dp/B08HJTL47C/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B08HJTL47C&pd_rd_w=sfVKh&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=pTqFK&pf_rd_r=0V9906PQ22PYFZ8P6NSF&pd_rd_r=62c3afff-fb92-4691-9274-67d91e9dfa91&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTk05NU1SUkVQNjNZJmVuY3J5cHRlZElkPUEwNjkwNDA2NTIyR0NLVDlDOUs1JmVuY3J5cHRlZEFkSWQ9QTA0Mjk1NjNRVVVZOFRNTUJHNE4md2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'))
