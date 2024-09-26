# What is a command

The command is a general term for the action that you wish to perform in the terminal.
A command can be simple or complex with the use of flags and arguments.

This sample command uses both flags and arguments to do a more than calling the application by its self.
```sh
firefox --new-window www.redhat.com
```

Breaking down the command the first component `firefox` is the application that is going to be executed.

The next component is a flag, `--new-window`. This tells firefox to open in a new window if there is currently an existing window.
There is a common pattern where flags that start with double dashes will be an actual word like `--new-window` or `--help`.
Or when the flag starts with a single dash, it will be a single character, like `-h`.
Normally the single dash flags can be chained together.
The following examples do the same thing, but one uses the single dash flags chained together.
```sh
ls --almost-all --size

# compare to

ls -As

# or even

ls -A -s
```

In the first example command the [www.redhat.com](www.redhat.com) is an argument to the `--new-window`.
An argument can be required on a flag or the command its self.
It is more common for applications to treat words as arguments over a sentence.
If you need to pass an argument to a command that with spaces by wrapping the string is quotes.
Double quotes are more the norm then using single quotes.
