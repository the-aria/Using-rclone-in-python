import subprocess
import os
# Rclone directory to be used as current working directory
rwd = r"U:\point\to\rclone"
# Rclone password
password="your rclone password"
#Remote that points to encrypted local data
enc_drive = "remotename:"
# Command that turns remote into virtual drive X: (mount)
# "--vfs-cache-mode writes" is not required for all cloud services
command = "rclone mount --vfs-cache-mode writes {} X:".format(enc_drive)
# Start new command prompt session in the correct directory
cmd_session = subprocess.Popen(['cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True,cwd=rwd)

# Give rclone the password so its not promped in the following mount procedure.
init_cmd = ['set RCLONE_PASSWORD_COMMAND=','set RCLONE_CONFIG_PASS={}'.format(password), command]
for cmds in init_cmd:
    cmd_session.stdin.write(cmds + '\n')
    cmd_session.stdin.flush()
# Close the CMD session
cmd_session.stdin.close()
cmd_session.wait()
# Get the output and error messages
output = cmd_session.stdout.read()
errors = cmd_session.stderr.read()
# Print the output and error messages
print('Output:')
print(output)
print('Errors:')
print(errors)

