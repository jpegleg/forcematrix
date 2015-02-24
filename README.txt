forcematrix, a code snippet

This thing, F O R C E M A T R I X, is just a calculator function code snippet.
Take an input file called /usr/local/lib/forcematrix.in and have it contain line delimited base 10 numbers.
F O R C E M A T R I X will run a series of simple calculations on numbers 1 through the value in the file.
If you use multiple lines, you will run the calulation again, 1 through the next value. The values from the file are F O R C E M A T R I X run ranges.

Example simple usage:
echo 9999 > /usr/local/lib/forcematrix.in
 /usr/local/scripts/forcematrix.py

Example advanced (heavy disk, heavy load) usage:
for x in {1..99999}; do echo "$x" > /usr/local/lib/forcematrix.in &&
/usr/local/scripts/forcematrix.py > /mnt/hadoop2/node-a-in-raw-matrix/forcematrix.out;
done

This is a neat test for python operations timing:
while true; do /usr/local/scripts/forcematrix.py > force.tmp && grep machine force.tmp | rev | awk '{print $2}' | rev >> pytime.log; done
