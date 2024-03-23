from bs4 import BeautifulSoup as bs
import smtplib
import requests
class Price:
    def check_price(url):
        try:
            header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US, en; q0.9",
            }
            sauce  = requests.get(url, headers=header)  
            soup   = bs(sauce.text, "html.parser")  
            name = soup.select_one(selector="#productTitle")
            prices = None
            if name:
                name = name.get_text().strip()
                prices = soup.find(class_="a-price-whole").get_text()
                prices = float(prices.replace(",", "").replace("₹", ""))
                print(name)
                print(prices)
            else:
                print("Error : Not Found")
                return None, None
            return prices, name
        except Exception as e:  
            print("Error:", e)
            return None, None 

    def send_email(message, sender_email, sender_password, receiver_email):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        s.sendmail(sender_email, receiver_email, message)
        s.quit()

    