import subprocess
import os
# 0.1 Rclone directory to be used as current working directory
rwd = r"U:\point\to\rclone"
# 0.2 Rclone password (if applies)
password="your rclone password"
# 0.3 Source folder
origin_root = r"U:\Data"
# 0.4 Rclone remote that encrypts and points to your desired remote
dest_root = "remotename:Data"
# 0.5 Base Input for CMD
command = "rclone copy --progress"
# 0.6 Year of data to be synced (Optional)
yy_str = str(21)
# 0.7 Directories inside origin_root that contain data to be encrypted\copied (Optional)
dirs_to_copy = ["AData", "BData", "CData", "OPTION"]

# 1.0 Start a CMD session
cmd_session = subprocess.Popen(['cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True,cwd=rwd)

# 1.1 Give rclone the password so its not promped in the following copy procedures.
init_cmd = ['set RCLONE_PASSWORD_COMMAND=','set RCLONE_CONFIG_PASS={}'.format(password)]
for cmds in init_cmd:
    cmd_session.stdin.write(cmds + '\n')
    cmd_session.stdin.flush()  

# 1.2 Create the correct path formats (Optional)
for dir_to_copy in dirs_to_copy:
    if dir_to_copy == "OPTION":
        origin_path = os.path.join(origin_root, yy_str + "File", dir_to_copy + yy_str)
        dest_path = os.path.join(dest_root, yy_str + "File", dir_to_copy + yy_str)
    else:
        origin_path = os.path.join(origin_root, yy_str + "File", dir_to_copy)
        dest_path = os.path.join(dest_root, yy_str + "File", dir_to_copy)
    # 1.3 Only copy directories that exist in origin (Optional)
    if not os.path.exists(origin_path):
        continue
    # 2.0 Create the full copy command with correct syntax for CMD
    copy_command=[command, "{}".format(origin_path), dest_path]
    full_command = ' '.join(copy_command)
    # 2.1 Run the copy command
    cmd_session.stdin.write( full_command + '\n')
    cmd_session.stdin.flush()   
# 2.2 Close the CMD session
cmd_session.stdin.close()
cmd_session.wait()
# 3.0 Get the output and error messages
output = cmd_session.stdout.read()
errors = cmd_session.stderr.read()
# 4.0 Print the output and error messages
print('Output:')
print(output)
print('Errors:')
print(errors)
input("Press Enter to exit...")