import sys, mechanize, lxml.html
filename = "example.txt"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
discount = 0.01 # todo - add percentage support

urls = {"United States":"https://camelcamelcamel.com/", "Canada":"https://ca.camelcamelcamel.com/", "United Kingdom":"https://uk.camelcamelcamel.com/", "Germany":"https://de.camelcamelcamel.com/", "France":"https://fr.camelcamelcamel.com/", "Italy":"https://it.camelcamelcamel.com/", "China":"https://cn.camelcamelcamel.com/", "Spain":"https://es.camelcamelcamel.com/", "Japan":"https://jp.camelcamelcamel.com/"}
# default_country = "United States" # todo - use default country

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
for ASIN in file: 
	ASIN = ASIN.rstrip('\n')
	print ASIN
	# Search for product
	for country, url in urls.items():
		br.open(url)
		br.select_form(nr=0)
		br.form["sq"]=ASIN
		br.submit()
		html = br.response().read()
		html = lxml.html.fromstring(html)
		# Verify ASIN was found
		if html.find_class("message"):
			print "Not found in " + country
		else: # Found! Break out of loop
			print "Found in " + country
			break
	# Get current price and calculate desired price
	price = html.find_class("black")[0].text
	price = price.replace("$","")
	price = float(price)
	desired_price = str(price-discount)
	print "Current Price: " + str(price)
	print "Desired Price: " + str(desired_price)

	# Set alert for desired price
	br.select_form(nr=1)
	br.form['price']=str(desired_price)
	br.submit()

	# Verify alert was set successfully
	html = br.response().read()
	html = lxml.html.fromstring(html)
	result = html.find_class("flash usermsg notice")[0][0].text
	result = result.strip()
	print result
file.close()