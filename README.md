# Logical Vulnerabilities

Dealing with user input can be a difficult task. Especially when the user has malicious intentions.
In this project we have some examples of programs with user input that can be exploited. The common ground for all of the examples is that the writer of the
program meant the user to input x but the user instead input y and thus hacking the program.

### Unsafe use of eval()
For example, a python program with the use of eval function in it. eval is very sensitive because if we can inject os.system() in it we can get full
control of the program.

### Unsafe use of pickle.load() 
Another example in this project is an unsafe use of python's pickle module. The pickle module allows us to define how the data will be pickled using __reduce__ function.
It returns a tuple of callable and arguments.
We can use the callable as os.system and the arguments as echo hacked (for example).
All this we put inside a class and pickled the class.
When the program unpickles it we get full control of the program.

### Bad parsing
Sometimes parsing the information from the user input can be done in a vulnerable manner. One such example is [here](q3).

### Time of Check to Time of Use
Sometimes user input validation takes a long time, and if we can manipulate the input data between the validation and execution 
we can pass the validation and execute whatever we want.
You can see that in action [here](q5).









