import requests

login = requests.get('https://login.squarespace.com/api/1/login/oauth/provider/authorize?client_id=qNgYXXcY8Fa8M&redirect_uri=https%3A%2F%2Fwww.squarespace.com%2Fauth%2Foauth%2Fconnect%3FdestinationUrl%3Dhttps%253A%252F%252Fwww.squarespace.com%252Fauth%252Fprotected-redirect%252Flogin%253Flocation%253Dhttps%25253A%25252F%25252Faccount.squarespace.com&state=1%3A1602773497%3AAyqUVgvT5DOqYk%2FYDeHKtOVUIPXESWO8DTra5Fjg3NE%3D&overrideLocale=en-US&options=%7B%22isCloseVisible%22%3Atrue%2C%22isCreateAccountViewActive%22%3Afalse%7D#/')
'''
heter all ordreinformasjon
GET https://api.squarespace.com/{api-version}/commerce/orders?modifiedAfter={a-datetime}&modifiedBefore={b-datetime}&cursor={c}&fulfillmentStatus={status}

Setter ordren til fulfilled
POST https://api.squarespace.com/{api-version}/commerce/orders/{id}/fulfillments

Trenger å oppdatere subscription til squarespace for å få gnerere api keys
'''