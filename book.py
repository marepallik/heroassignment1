Book1_price = 499.00
Book2_price = 855.00
Book3_price = 645.00
n1=int(input('enter no of book1 needed: '))
n2=int(input('enter no of book2 needed: '))
n3=int(input('enter no of book1 needed:'))
subtotal=Book1_price*n1+Book2_price*n2+Book3_price*n3
gst=0.12
taxes=subtotal*gst
delivery_charges=250.00
total_invoice=subtotal+taxes+delivery_charges
print(subtotal)
print(taxes)
print(total_invoice)