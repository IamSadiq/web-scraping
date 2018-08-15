import re
from bs4 import BeautifulSoup

data = """
<html>
    <head>
        <title>My Sample Page</title>
        <script>
        $.ajax({
            type: "POST",
            url: 'http://www.example.com',
            data: {
                email: 'abc@g.com',
                phone: '9999999999',
                name: 'XYZ'
            }
        });
        </script>
    </head>
    <body>
        <h1>What a wonderful world</h1>
    </body>
</html>
"""

soup = BeautifulSoup(data, 'lxml')
script = soup.find('script')

pattern = re.compile("(\w+): '(.*?)'")
fields = dict(re.findall(pattern, script.text))
print(fields['email'], fields['phone'], fields['name'])