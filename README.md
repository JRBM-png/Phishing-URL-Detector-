# Phishing-URL-Detector
A url is scored against several phishing flags

## Overview:

When using any url it checks against 7 rules producing a score instead of a yes/no verdict. This is because detection has multiple layers and seeing exactly what failed and why it failed delivers more useful information

## The Rules:
1) Character length; Most url's are under 75 characters long, if url's are excessive in length it could be due to filler words hiding after the initial link to deceive users and take them to a different landing page

2) '@' Symbol; In browsers everything before the '@' symbol can be ignored, this can be used to disguise the real destination for example 'https://reallink@fakelink.com'. The part before the @ would be something recgonised and trusted like a bank whilst the part after the @ would be the attackers link

3) Encrypted; url's starting with 'https://' transmit data with encryption providing an extra layer of security. Websites with this don't necessarily mean they are secure since you can get a certificate for your website, however combined with the other steps it can reveal if the website can be trusted or not.

4) Hyphen Count; Similar to the @ symbol, a url with excessive hyphen's can be used to make a fake domain look convincing by stringing words together. An example of this would be 'paypal-secure-login-account.com'.

5) Suspicious Words; Within url's there are some words that can be deemed as suspicious, while this isn't the case every time, some words together or mixed in can be a red flag. Words like "verify", "secure", "login", "confirm" can be used to create panic or a sense of urgency for users, and without thinking they will click the link.

6) IP address detection; Most trusted domains don't have a raw IP address, it will have a domain name, such as 'bankname.com' however sometimes a raw IP address is used instead as it's cheaper than to rent a domain name. Additionally with the earlier methods such as hiding the real destination with the '@' symbol, by detecting if there is an IP address in the link it can show the hidden destinations.

7) Typo squatting; 
