#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/18 0018 21:02
import re

import requests

temp_variables={'token': '58_r6tlBnDN5wDoM1wBsH-x5XmvEvjNjl5ai5u9mZorIluaoAd8hxbALZu-q9DeWlYwXaIAH90eziXF0QG9phM_1tutgry_mr4jIrfyoXlPVaqDGEZVTMLb3BAIPx-JSPbvqovisrJYS4gZs9nDHHFeAGAXXV'}

params = '{"access_token":"${token}","sdasd":""${1231}"}'
value = re.findall('\\${\w+}',params)[0]
print(value)
params = params.replace(value,temp_variables['token'])
print(params)


# requests.get()