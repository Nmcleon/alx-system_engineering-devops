0x02. Shell, I/O Redirections and filters
# Shell, I/O Redirection

## What do the commands head, tail, find, wc, sort, uniq, grep, tr do

The commands head, tail, find, wc, sort, uniq, grep, tr perform various operations on text files.

* `head`: Prints the first few lines of a file.
* `tail`: Prints the last few lines of a file.
* `find`: Searches for files or directories.
* `wc`: Counts the number of lines, words, and characters in a file.
* `sort`: Sorts the lines of a file.
* `uniq`: Prints only the unique lines in a file.
* `grep`: Searches for a pattern in a file.
* `tr`: Translates characters in a file.

## How to redirect standard output to a file

To redirect standard output to a file, you can use the `>` operator. For example, the following command redirects the output of the `ls` command to a file named `my_files.txt`:

```bash
ls > my_files.txt
```

## How to get standard input from a file instead of the keyboard

To get standard input from a file, you can use the `<` operator. For example, the following command takes the input from the file `my_input.txt` and uses it as the input for the `sort` command:

```bash
sort < my_input.txt
```

## How to send the output from one program to the input of another program

To send the output from one program to the input of another program, you can use a pipe (`|`). For example, the following command takes the output of the `ls` command and pipes it to the `grep` command, which searches for the word `'README.md'` in the output:

```bash
ls | grep 'README.md'
```

## How to combine commands and filters with redirections

You can combine commands and filters with redirections to create complex pipelines. For example, the following command takes the output of the `ls` command, pipes it to the `grep` command to filter for files that end with `.txt`, and then redirects the output to the `wc` command to count the number of lines in the filtered output:

```bash
ls | grep '\.txt$' | wc -l
```

## Special Characters

Special characters are characters that have a special meaning in the shell. Some common special characters include:

* `blank space`: Separates words in a command.
* `single quote`: Prevents words from being expanded or interpreted by the shell.
* `double quote`: Prevents words from being expanded, but allows them to be interpreted by the shell.
* `backslash`: Escapes a character, meaning that it is not interpreted as a special character.
* `comment`: Indicates that the rest of the line should be ignored by the shell.
* `pipe`: Sends the output of one command to the input of another command.
* `command separator`: Separates commands in a shell script.
* `tilde`: Expands to the home directory of the current user.

## Other Man Pages

* `man echo`: How to display a line of text.
* `man cat`: How to concatenate files and print on the standard output.
* `man rev`: How to reverse a string.
* `man cut`: How to remove sections from each line of files.
* `man passwd`: What the `/etc/passwd` file is and what its format is.
* `man shadow`: What the `/etc/shadow` file is and what its format is.
