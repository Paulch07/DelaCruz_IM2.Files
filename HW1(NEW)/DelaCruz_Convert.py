def convert_currency(usd):
    pound = usd * 0.74      
    inr = usd * 88.25     
    yuan = usd * 7.12     
    return pound, inr, yuan


while True:
    amount = input("Enter USD amount(s) separated by comma (* to exit): ")
    
    if amount == "*":
        print("bye.")
        break

    amounts = amount.split("@")
    
    print("USD\tINR\tYuan\tPound")
    for dollar in amounts:
        dollar = dollar.strip()
        if dollar:
            usd = float(dollar)
            pound, inr, yuan = convert_currency(usd)
            
            print(f"{usd}\t{inr}\t{yuan}\t{pound}")
    print()