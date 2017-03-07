# camelcamelcamel-import
Import Amazon Standard Identification Numbers (ASIN) on camelcamelcamel.com

mechanize and lxml are required:
```
pip install mechanize
pip install lxml
```

Running example.txt:
```
$ python camelcamelcamel-import.py 
B01JRTEWH6
Not found in United States
Found in Canada
Current Price: 12.74
Desired Price: 12.73
You have tracked the 3rd Party New Price for ThermoPro TP03A Digital Thermometer Instant Read Food Meat Thermometer for Kitchen Cooking BBQ Grill Smoker and Bath Water (Battery Included)
B00CIECDEM
Found in United States
Current Price: 25.0
Desired Price: 24.99
You have tracked the Amazon Price for SUBWAY Gift Card $25
B00BXLW38M
Found in United States
Current Price: 50.0
Desired Price: 49.99
You have tracked the Amazon Price for Starbucks Gift Card $50
```