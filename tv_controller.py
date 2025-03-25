import subprocess

is_tv_on = False

def tv_turn_on():
    # subprocess.run(["echo", "on 0", "|", "cec-client", "-s", "-d", "1"])
    subprocess.run(["echo on 0 | cec-client -s -d 1"], shell=True)
    is_tv_on = True

def tv_turn_off():
    # subprocess.run(["echo", "standby 0", "|", "cec-client", "-s", "-d", "1"])
    subprocess.run(["echo standby 0 | cec-client -s -d 1"], shell=True)
    is_tv_on = False
