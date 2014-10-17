schemer
=======

python port of /thefryscorer/schemer
using python 2.7


Run main.py
--

python main.py gnome /path/image.ext

Example output color preview image:
--

![alt tag](https://raw.github.com/ghidra/schemer/master/example_color_output.png)
outside border is the darkest color, and used and the background color
the little square in the top left if the lightest color, and used as the foreground color

Example output command:
--
this should be copied from the terminal window and pasted at the command line and run:

gconftool-2 -s -t string /apps/gnome-terminal/profiles/Default/palette /#383819192B2B:#8B8B21212B2B:#C5C56A6A4B4B:#ADAD3B3B3131:#A3A35D5D4444:#ACAC1C1C1C1C:#B5B58E8E5555:#6060D0D1717:#C8C8AAAA6464:#7B7B3C3C3535:#7D7D00808:#C7C729292626:#D4D4BBBB7B7B:#B2B200909:#CBCB4F4F3333:#888882825252
gconftool-2 -s -t string /apps/gnome-terminal/profiles/Default/background_color /#cdcdd2d28f8f
gconftool-2 -s -t string /apps/gnome-terminal/profiles/Default/foreground_color /#2020a0a1717

Notes:
--

Currently, I am assuming Ubuntu only.
the above commands set the colors after running the gconftoll-2 commands.
Ultimately I would want to just automatically set the colors in the ~/.gconf/apps/gnome-terminal/profiles/Default text file, but doing so doesnt seem to make a difference. I think that the above commands set it to a global config file that I havent found.

Other operating system, I can make it work if you can tell me what command I should return, or potentially what file I should edit to make this a simple single command tool.
