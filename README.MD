# SYS_SCAN

Thak you for checking out this project.

This script aims to help with remote machine recon in a CTF once you have gained access.

### Currently implamented:
    Get current user
    Test if able to get sudo info
    Test current pwd
    If /home in pwd, scan for all folders

### Future implamentation:
    Recursive search through /home for .ssh folder and potential keys (scan)
    Search for SUID (test)
    Search for GUID (test)
    Scan for any open listening ports (scan)
    See if environment is in a docker container (test)
    Add in help option that users can requets info on specific test adn scans (feature)

# IMPORTANT!!

Do not be a script kiddie!

Yes, use this tool if you want to or you are still having a hard time at first.

But do not use without learning.

Learn what the code is doing.
What it is teting for.
What it is scanning for.

So that way, you can run the commands on your own and understand.
