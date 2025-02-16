---
order: 4
icon:
  type: bitcoin-icons:linux-terminal-filled
---
# What is sudo

`sudo` is an administrative command that allows the user more permissions over the system.
Caution should be used when running any command with `sudo` as you change the system for all users.

With great power comes great responsibility.

Running commands with the elevated permissions will require entering the user's password.
When on the terminal when an application request a password the user input will be hidden.

The elevated permissions are only granted for that run of the command.
Any following commands that require elevated permissions will also require being prefixed with `sudo`.

However, the input of the password may not be required for the following commands if ran in a short enough timeframe.

