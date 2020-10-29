# amazon-price-down-tracker
This program will track a product cost of the given amazon product url 
and send emails updates to the target's email by given email and password 

updates are:-
  1. starting (once only) 
  2. weekly (every week with graphical representaion) 
  3. Instantaneous (If the cost change)
  
## provide graph of the data every week
**program will attach the line graph of the cost with days to study changes with the weekly email**

## Email representation

### first time (only once -to notify that services are started)
<img width=600 src='https://github.com/rishabhjainfinal/amazon-price-down-tracker/blob/main/README_dependency/first-time.png' alt='first time mail template' >


### Error mail
<img width=600 src='https://github.com/rishabhjainfinal/amazon-price-down-tracker/blob/main/README_dependency/error.png' alt='error mail template'>

### update or weekly notification (with graph and price_data.json attached to the email)
This mail attached with graph of pice change and json file for more info.
  1. [EXMPLE graph](README_dependency/graph.png)
  2. [EXMPLE price_data.json](README_dependency/price_data.json)


<div style='display:flex;'>
  <img width=600 src='https://github.com/rishabhjainfinal/amazon-price-down-tracker/blob/main/README_dependency/update.png' alt='update mail template' >
  <img width=300 src='https://github.com/rishabhjainfinal/amazon-price-down-tracker/blob/main/README_dependency/graph.png' alt='graph representation' >
</div>



# Usage
```
git clone https://github.com/rishabhjainfinal/amazon-price-down-tracker.git
cd amazon-price-down-tracker/
```

----

# On server 
For running the program on a server use `nohup` before 'python' to run even after you ssh-out example:- 

`nohup python runner.py -f sec.txt`

## Arguments
`python runner.py -h`

```
D:\amazon_price_down_tracker>python runner.py -h
usage: runner.py [-h] [--intro] [-u URL] [-a USER] [-p PASSWORD] [-t TARGET] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  --intro               give brief intro of the program
  -u URL, --url URL     url of the product to track
  -a USER, --user USER  user-email-address@gmail.com
  -p PASSWORD, --password PASSWORD
                        password of the user-email-address@gmail.com
  -t TARGET, --target TARGET
                        target email address
  -f FILE, --file FILE  file name if data is saved into file
```

----

### Info about the program

`python runner.py --intro`

---

### Passing the arguments in command line [example] 

`python runner.py -u url_of_the_product -a userEmail -p password_of_user -t target_email `

---

### You can save all the information in a file then you can pass -f to seek from a file

`python runner.py -f sec.txt`

**sec.txt**
```
username = <your-email-address>
password = <your-password>
target = <your-target-email-address ('it may be same as username')>
url = <product-url-you-wanna-track>
```
---
