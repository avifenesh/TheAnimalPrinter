How to use:

you can find the requirements for create the env file in the requirements.txt file

the program take url path as an argument, check for animal table there, for
each animal download the relevant image into tmp folder, and output the
name, the collateral adjective and the local path to the pic

Im trying to avoid comment in my code and write self-explained code instead
I've been trying to do that in this project also
I'll explain the code here and the train of thought, in case that it doesnt
clear in the code itself

The main file take the arguments from the user, validate it and provide it to
 the printer function

The printer function is the big-boss function, that call to the other
function to d there job in their time

first we create the file and directory we'll for later - the tmp directory
and the html file with opening content

Using requests and bs4 the program get the html from the page and process it

"find table" function find the desirable table, by searching for the
key-word in the header

output_animals_and_pic function go over the table find the data we looking for
and create threads-array of download-pic and output to html file processes

then we run all the threads and letting the user know that everything worked
 fine

in the tests file i've created few unit-test to check the small parts work
fine and can handle with edge-cases

that about all, more or less