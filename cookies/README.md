In this challenge, we are given the following webpage:
http://mercury.picoctf.net:54219/

When we send the request, it sends a cookie with an attribute called "name". If we change the value from 0 and onwards, it gives a different name of cookie

I just iterated until I got no more cookies with the iterate_requests script and then looked for a flag with a search command
