import re

text = "The price is $45.99 USD. The old price was $55.00 USD."
# Extract text between "$" and " USD"
pattern = r"(?<=\$)\d+\.\d+(?= USD)" 

prices = re.search(pattern, text)
print(prices)
# Output: ['45.99', '55.00']
