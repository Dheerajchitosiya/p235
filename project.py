import requests
for i in range(1,5000):
    url=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    x=requests.get(url=url)
    if x.status_code==200:
        print(url)