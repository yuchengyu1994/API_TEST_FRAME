#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/18 0018 13:43
import jsonpath



d1 = {"access_token":"58_HmEhna-S4VZ6rgI5vp6iSBzNiTCcVanxRBEdYGvY-Zl60lTxJtJiKcsL5pJ0eEIVkSN5ZD7o7SMo-IaQBFIaNdfZ7blyfCangvMYlI7TyP75l4K2dgPYVHFdc-N8P4Ou_DYzZaIXyfWZ0V5XXWBjAIATSX","expires_in":7200}
str1 = jsonpath.jsonpath(d1, '$.access_token')
print(str1)
