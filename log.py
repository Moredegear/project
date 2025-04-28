with open("log.txt", 'w',encoding="utf-8") as f:
    f.write("Hello World")
with open("log.txt", 'r',encoding="utf-8") as f:
   text = f.read()
   print(text)
with open("log.txt", 'a',encoding="utf-8") as f:
    f.write(" Hello World")
with open("log.txt", 'r',encoding="utf-8") as f:
   text = f.read()
   print(text)
shopp = ["apple","bannan","cox"]
shop = ', '.join(shopp)
with open("shopping_list.txt", 'w',encoding="utf-8") as f:
    f.write(shop)
with open("shopping_list.txt", 'r',encoding="utf-8") as f:
   text = f.read()
   print(text)
shopp_1 = ["meso","milk","srobvery"]
shop_1 = ', '.join(shopp_1)
with open("shopping_list.txt", 'a',encoding="utf-8") as f:
    f.write(f", {shop_1}")
with open("shopping_list.txt", 'r',encoding="utf-8") as f:
   text = f.read()
   print(text)




