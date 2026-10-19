def selling_price(marked_price,discount):
    discount_amount = marked_price*discount/100
    price = marked_price - discount_amount
    return price
print(selling_price(1200,15))