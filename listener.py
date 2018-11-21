from pynput.keyboard import Key, Listener

string_key = []
accepted_keys = {line[:-2] for line in open("/home/adryel/Desktop/test_directory/file.txt")}
print([i for i in accepted_keys])

def on_press(key):
    global string_key
    print("{0} pressed".format(key))
    if key is not Key.enter:
        if key not in [Key.shift, Key.shift_l, Key.caps_lock]:
            string_key.append("{0}".format(key))
    else:
        result = ''.join(string_key)
        result = result.replace("\'", "")
        print("{}".format(result) if result not in accepted_keys else "Accepted Key")
        string_key = []


def on_release(key):
    # print('{0} released'.format(key))
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()