# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > Command | Function
--- | ---
`pwd` | show current working directory path
`mkdir <directory>` | creating a directory
`rmdir <directory>` | deleting a directory
`touch <file>` | creating a file using `touch` command
`rm <file>` | deleting a file
`rm -f <directory>` | force deleting a directory
`mv <file_old> <file_new>` | renaming a file
`mv <file> <directory>` | moving a file from one directory to another
`ls -a` | listing hidden files
`cp <file> <directory>` | copying a file from one directory to another

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > Command | Function
--- | ---
`ls` | list files in the current working directory 
`ls -a` | list all files including hidden files 
`ls -l` |  list the long format listing
`ls -lh` | 	list long format with readable file size
`ls -lah` | list long format with readable file size including hidden files  
`ls -t` | list newest files first. (based on timestamp)  
`ls -Glp` | list long format directory in color and with / at the end 
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 

`ls -la`
`ls -r`
`ls -d`
`ls -c`
`ls -Glp`
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` reads items from the standard input, delimited by blanks or newlines, and executes the command (press ctrl-D). Blank lines on the standard input are ignored.

Use `find` and `xargs` to search for files that contain a specific string. Ex: `$ find /Users -name "*.py" | xargs grep "by Winnie"`
 

