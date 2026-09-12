score = 0
url = "https://youtube.com/"
len(url)

#Here are a few examples you can use down below!
#https://youtube.com/
#https://www.google.com/
#192.168.1.1
#mail.staging.example.com
#https://amaz0n.com/login

if len(url) > 75:
    score += 1
    print(f"The url is too long ({len(url)} characters) and may be suspicious.")
   
else:
    print(f"url length is acceptable ({len(url)} characters).")

if "@" in (url):
    score += 1
    print("url contains '@' may be disguising real destination")
    
else: 
    print("url does not contain '@' may be safe")

if (url) .startswith("https://"):
    print("Secure connection")

else:
    score += 1
    print("url is unencrypted potential red flag")

if (url) .count("-") > 2:
    score +=1
    print ("url hyphen count is suspicious")

else:
    print("url hyphen count is acceptable")

suspicious_words = ["verify", "secure", "login", "account", "update", "confrim", "banking"]

found = False

for word in suspicious_words:
    if word in (url):
     found = True

if found:
    score += 1
    print("url contains one or more suspicious words")

else:
    print("url contains no suspicious words")

prefixes = ["https://", "http://"]

for prefix in prefixes:

    if url.startswith(prefix):
        url = url.replace(prefix, "")

parts = url.split ("/")  
domain = parts [0]
#print(domain)

ip_parts = domain.split(".")
#print(ip_parts)

if len(ip_parts) == 4:
    print("url has correct amount")

    all_digits = True
    for segment in ip_parts:

        if segment.isdigit() == False:
            all_digits = False

    if all_digits:
        score += 1 
        print ("all digits")

    else:
        print("not all digits")

else:
    print("domain does not resemble a raw IP address, safe")

from difflib import SequenceMatcher

known_domains = ["amazon.com", "google.com", "WhatsApp.com"]

found = False

for legit_domains in known_domains:
    similarity = SequenceMatcher(None, domain, legit_domains).ratio()
    #print(similarity)
    if similarity > 0.85 and similarity < 1.0:
        found = True

if found:
    score += 1
    print("url similarity is above threshold")

else:
    print("url similarity below threshold")

print(f"Total red flags triggered: {score}/7")