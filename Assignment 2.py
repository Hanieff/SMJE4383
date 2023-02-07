import re
import csv
import pytesseract
import cv2

# Load the image file
image = cv2.imread("Invoice.webp")

# Recognize the text in the image using OCR
text = pytesseract.image_to_string(image)

# Extract bill to information
bill_to = re.search("Bill to: ([\w\s&]+[\.])", text).group(1)

# Extract invoice number
invoice_number = re.search("Invoice No: (\d+)", text).group(1)

# Extract date
date = re.search("Date: ([\d\w\s,]+\d{4})", text).group(1)

# Extract items
items = re.findall("(\d+)[\s.]+([\w\s]+\$)", text)

# Extract total
total = re.search("Total (\$\d+)", text).group(1)

# Format items
formatted_items = []

for item in items:
    data = item[1].replace("$", "")
    formatted_item = re.sub( r'\d', '', data)			
    formatted_items.append(formatted_item)
    
# Remove the last item "Total"
formatted_items.pop()

# Print results
print("Bill to: " + bill_to)
print("Invoice No: " + invoice_number)
print("Date: " + date)
print("Item: " + str(formatted_items))
print("Total: " + total)

# Write the extracted data to a CSV file
file_name = input("Enter the name of the CSV file: ")

with open(f'{file_name}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(["Bill To", "Invoice No", "Date", "Item", "Total"])
    
    # Write data row
    writer.writerow([bill_to, invoice_number, date, formatted_items, total])

