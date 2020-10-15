'''file for requesting information from squarespace
first learning how to extract infromation from an API'''
import requests

r = requests.get('https://xkcd.com/353/')

#print(r) #prints the response from the webpage

#accessing content
#print(dir(r))

#For more details about a response object:
#print(help(r))

#printing unicode
#print(r.text)

'''
downloading an image, as bites 
image = requests.get('https://imgs.xkcd.com/comics/python.png') 
with open('comic.png', 'wb') as f:
     f.write(image.content)
writes the imagebytes to the directory as an image
r.ok returns true for any response les than 400
as these are the errors that are not client
server errors
'''
#new webpage for testing, responds with json info
payload = {'page': 2, 'count': 25}
req = requests.get('https://httpbin.org/get',params=payload)
#passing som url parameters
#print(req.text)
#print(req.url)
#posting to an url
payload2 = {'username': 'someusermame', 'password': 'somepassword'}
req = requests.post('https://httpbin.org/post',data=payload2)
#can do the same with put
#print(req.text)
'''
creating a dict of the json response
req_dict = req.json() 
print(req_dict)
'''

login = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
print(login.text)




