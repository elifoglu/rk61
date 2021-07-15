choices = ["@", "#", "|", "~", "$", "[]", "{}", "\\"]

retCode, choice = dialog.list_menu(choices)
if retCode == 0:
    keyboard.send_keys("" +choice)

# @1
# |2
# #3
# $4
# \5
# ~6
# {7
# [8
# ]9
# }0