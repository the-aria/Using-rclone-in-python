# Using-python-to-run-rclone

## Description

This repository contains two Python scripts that enable secure data transfer and access using rclone, a command-line program for cloud storage management. The first script, **EncryptAndUpload.py**, copies data from the *origin_root* directory and transfers it to an encrypted remote using the rclone copy command. Assuming the rclone remote is set up as a "crypt" type remote, the command "rclone copy" encrypts the data as well. The second script, **MountEncryptedData.py**, utilizes the rclone mount command to create a virtual drive, making the encrypted data accessible to the user.

## Prerequisites

Before using these scripts, ensure that the following dependencies are installed:

- **rclone:** This tool is required for managing cloud storage. Install it from the official rclone website: [rclone.org](https://rclone.org/downloads/).
- **Python:** The scripts are written in Python. Install Python from the official Python website: [python.org](https://www.python.org/downloads/).
- **WinFsp:** This is a dependency for rclone on Windows systems. Install it from the official WinFsp website: [winfsp.org](https://github.com/billziss-gh/winfsp/releases).

Additionally, during the installation process for rclone, ensure that the installation path is set to "rwd" as specified in our code.

## Configuration

This repository assumes that the user has properly set up rclone, including the configuration of remotes and other necessary settings. It is important to configure rclone according to your specific cloud storage provider and desired encryption settings. Please refer to the rclone documentation for detailed instructions on configuring rclone: [rclone.org/docs](https://rclone.org/docs/).

## Optional Code

The file **EncrypAndUpload.py** includes optional code for users who wish to backup a collection of folders. This code can be customized and extended to include specific folders for backup. Modify the script according to your backup requirements, ensuring the folders are correctly specified.

## Usage

1. Clone or download this repository to your local machine.
2. Install the required dependencies mentioned in the "Prerequisites" section.
3. Ensure that rclone is properly configured and the remotes are set up according to your needs.
4. Modify the script files as necessary, providing the appropriate paths and configurations.
5. Run **EncryptAndUpload.py** to encrypt and upload data to the specified remote.
6. Run **MountEncryptedData.py** to mount the encrypted data as a virtual drive for easy access.

Please note that it is essential to review and understand the scripts before running them to ensure they align with your specific use case.

## License

GNU General Public License v3.0

## Contributions

All input and contrubutions are welcome!

## Troubleshooting

In case of any issues or errors, refer to the following troubleshooting steps:

1. Check if all the dependencies are correctly installed and up to date.
2. Review the rclone configuration and ensure that the remotes are set up properly.
3. Verify the paths and configurations in the script files.
4. Consult the rclone documentation or relevant online resources for further assistance.

If the issue persists, feel free to open an issue in the repository, providing detailed information about the problem encountered.

Good luck :)
