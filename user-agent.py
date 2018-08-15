"""
 Background on UserAgents -- UserAgents make requests of user's behalf. E.G Our browsers
 With every request made to a website from our browsers, the browser attaches a user-agent
 key / value pair to the headers and hence tell the site which user-agent is making such
 request to their server.

 However, when we make requests using Python's 'requests' library, no user-agent attribute
 is sent along, as such most websites are able to know that a robot is making a request to
 their server, and as a result they may prevent our scripts from making our request.

 But with 'fake-useragent', we can Fake a UserAgent and act as a browser when making our 
 requests, without the sites knowing.
"""

import requests
from fake_useragent import UserAgent

ua = UserAgent()

header = {'user-agent': ua.chrome}
# print(ua.chrome)

page = requests.get('http://www.google.com', headers=header)
# print(page.content)

"""
Timeouts are used to give our script a timing for when to end a request that is taking too long to respond
Background on Timeouts -- it is advisable to use timeouts in multiples of 3
"""
page = requests.get('http://www.google.com', timeout=3)