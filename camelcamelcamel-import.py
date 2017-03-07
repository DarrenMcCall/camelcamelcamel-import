import sys, mechanize, lxml.html
filename = "example.txt"
username = "YOUR_USERNAME_HERE"
password = "YOUR_PASSWORD_HERE"
discount = 0.01

# Login
br = mechanize.Browser()
br.set_handle_robots(False)
br.open("https://camelcamelcamel.com/login")
br.select_form(nr=1)
br.form["login"]=username
br.form["password"]=password
br.submit()

# Verify username and password
html = br.response().read()
html = lxml.html.fromstring(html)
if html.find_class("flash usermsg error"):
	print "Your username or password was entered incorrectly."
	sys.exit()

file = open(filename, "r")
for line in file: 
	line = line.rstrip('\n')
	# Search for product
	br.open("https://camelcamelcamel.com/")
	br.select_form(nr=0)
	br.form["sq"]=line
	br.submit()

	# Get current price
	html = br.response().read()
	html = lxml.html.fromstring(html)
	price = html.find_class("black")[0].text
	price = price.replace("$","")
	price = float(price)
	desired_price = str(price-discount)

	# Set alert
	br.select_form(nr=1)
	br.form['price']=str(desired_price)
	br.submit()

	# Check result
	html = br.response().read()
	html = lxml.html.fromstring(html)
	result = html.find_class("flash usermsg notice")[0][0].text
	result = result.strip()
	print result + " @ " + desired_price
file.close()
