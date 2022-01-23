Link to challenge: https://play.picoctf.org/practice/challenge/105?page=1

For this challenge, you have C code that reads a file that seems to contain the flag on a server. In a section of it, there is a highly unsecure method to printing information

scanf("%300s", &variable);
printf(variable);

Why is this insecure? Well, because you can pass parameters to the printf directly from the scanned text. Writing %s and pressing enter will cause the printf statement to print whatever string like thing might be on the stack. Passing %x will print the current byte on the top of the stack in hexadecimal. Knowing that the flag was read from a file to non reserved memory, we can assume that the flag will be in the stack.

Now, we can just pass tons of %x into the input to get a look on the stack. We get lots of gibberish, but among it, there are some characters that will look like a picoCTF flag 'icopFTC{...' (you have to convert it from hexadecimal to ascii first)

I am not fully sure of the reason of the inversion. Perhaps it is a consequence of being saved in a structure like a stack? Nevertheless, taking the flag in groups of fourth bytes and inversing it gives us the flag.


