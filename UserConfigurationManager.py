def add_setting(dict_setting, tup_keyvalue):
    if tup_keyvalue[0].lower() in dict_setting:
        return(f'Setting \'{tup_keyvalue[0].lower()}\' already exists! Cannot add a new setting with this name.')
    else:
        dict_setting[tup_keyvalue[0].lower()] = tup_keyvalue[1].lower()
        return(f'Setting \'{tup_keyvalue[0]}\' added with value \'{tup_keyvalue[1]}\' successfully!')


def update_setting(dict_setting, tup_keyvalue):
    if tup_keyvalue[0].lower() not in dict_setting:
        return(f'Setting \'{tup_keyvalue[0].lower()}\' does not exist! Cannot update a non-existing setting.')
    else:
        dict_setting[tup_keyvalue[0].lower()] = tup_keyvalue[1].lower()
        return(f'Setting \'{tup_keyvalue[0].lower()}\' updated to \'{tup_keyvalue[1].lower()}\' successfully!')



def delete_setting(dict_setting, chkkey):
    if chkkey.lower() in dict_setting:
        del dict_setting[chkkey.lower()]
        return(f'Setting \'{chkkey.lower()}\' deleted successfully!')
    else:
        return('Setting not found!')
    

def view_settings(dict_setting):
    if len(dict_setting) == 0:
        return('No settings available.')
    else:
        return("Current User Settings:\n"+ "\n".join([f"{k.title()}: {v}" for k, v in dict_setting.items()])+"\n")

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))