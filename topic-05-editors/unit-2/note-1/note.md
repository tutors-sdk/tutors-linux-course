# Why use Vim?

What good reason is there to know Vim?

## What good reason is there to know Vim?

Out of the box, vim does not look great and nano seems to be better.
Vim is not easy, and there is a steep learning curve to using it, but when you get the basics down it becomes extremely fast.

Vim Motions allow for very fast movement within a file. 
In the lab, the commands used were very basic, with time, as your knowledge expands, so does your move moments.

Take the following example where we add a new print to the `hello.py`, which is in the state as bellow.

```python
def hello(name):
  print(f'hello {name}')
  print('hello from nano')
  print('hello from vi')

if __name__ == '__main__':
  hello('world')
```

Try this command `:4 ENTER Vyp fh ct'` and add the string `vim can be fast`.
The command may seem overly complicated, how could anyone remember such a thing ?
Let's break down the command.

- `:4 ENTER` goes to the fourth line.
- `V` visually selects the whole line where the cursor is.
- `y` yanks (copies) the selected text.
- `p` pastes the yanked text. As it is a whole line, it is pasted below the current line.
The cursor is also moved to the newly pasted text.
- `fh` finds the next `h` on that line.
- `ct'` change till `'`, 

## But it looks so old.

The out-of-the-box experience is not great, and it would even be recommended that you use a more modern version of vim, such NeoVim.
Below is a screenshot of NeoVim that has being configured.

![Personal NeoVim](img/personal_neovim.png)

## Vim motions are almost a standard

With the number of years that vim has being around a lot of tools have adopted to use the same keybinding.
This means understanding the motions for one tool can help with many other tools.

`/` when used in normal mode it will open the search prompt.
The `/` is used in many other tools, for example.
If we cat the hello.py file into less using pipes, we can use the `/` to search the file.
For now, this may look like a complex command that uses a concept call pipes. 
Pipes are covered later.
For now, some trust is needed.

Below is the command.
```sh
cat hello.py | less
```

This will open the file in a pager (less).
Now press `/` and type in `hello` followed by `ENTER` to search the file.
This will highlight the instances of `hello` within the file.
You can move forward through the instances with `n` and backwards wit capital `N`.
While these commands were in the application less, they are the very same commands from vim.

There are many more examples like this which make it good to know the vim motions.

