while True :     # donguye girmesi icin True degeri verdik
    number = input("enter a positive number: ")
    digits = len(number)  # digits karakterlerin hepsi rakam mi? 
                          # len ile rakamin uzunlugu kadar, sayilarimizin ustune alacagiz
    summ = 0  
    if not number.isdigit():  #  true cikmasi ve kosulu saglayip asagi inmesi icin not degeri verdik
        print(number, "is invalid entry. enter numeric value!")
    elif int(number) >= 0:   # kosulumuza uydu ve sifirdan buyukse dönguye sokacagiz
        for i in range(digits) :   
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :   #  esit olup olmadigini kiyasliyoruz
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break