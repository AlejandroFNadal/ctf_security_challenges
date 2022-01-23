Challenge: https://play.picoctf.org/practice/challenge/163?page=1

We get a file called static. Opening it in nano reveals a 'ELF' text at the begining that reveals that we are dealing with an executable

The ltdis.sh file is also given to us. We can see that will try to dissassemble the executable. The flag -Dj will dissamble all and then get the .text section. 

If it can be done, the script later takes all the strings from it with the strings command. The -t x flag will gives us the offset in hexadecimal

And that is all. Running the command will yield the flag among many other text lines.


