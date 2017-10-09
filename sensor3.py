from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'XkhvEVc39LqEMGCLKkUH7GUCw'
CONSUMER_SECRET = 'hWBkIakyQLzmElCDYzg9fjFDcM551TPyWZ9v0lkOXBTcaY4xC5'
ACCESS_TOKEN_KEY = '912202866571354113-NAfE0j8qQisrP2z4nzzJmKUYbgJVawY'
ACCESS_TOKEN_SECRET = 'ILmEfoaxAgi7UXjWZJty2BAlXRhVFVxmd4tPSaOJsw42J'


while True:
    
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open('/home/pi/cam/imgs/cod.jpg')
    print('done')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
    print(r.status_code)

