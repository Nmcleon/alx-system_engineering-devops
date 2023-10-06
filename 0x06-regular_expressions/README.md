# 0x06-regular_expressions
# Regular Expressions

This repository contains a series of Ruby scripts that work with regular expressions. Each script focuses on specific regular expression patterns and matching requirements. Below is an overview of each script and its purpose.

## 0. Simply Matching School

This script matches the word "School" using a regular expression. It accepts one argument and passes it to the regular expression matching method.

**Example:**

```bash
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

## 1. Repetition Token #0

This script finds the regular expression that matches certain patterns based on repetition tokens. It accepts one argument and passes it to the regular expression matching method.

## 2. Repetition Token #1

Similar to the previous script, this one focuses on finding the regular expression that matches specific patterns using repetition tokens.

## 3. Repetition Token #2

Continuing with repetition tokens, this script identifies the regular expression that matches particular patterns.

## 4. Repetition Token #3

This script's goal is to find a regular expression that matches certain patterns without using square brackets.

## 5. Not Quite HBTN Yet

The regular expression in this script matches strings that start with 'h,' end with 'n,' and can have any single character in between. It accepts one argument and passes it to the regular expression matching method.

**Example:**

```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
```

## 6. Call Me Maybe

This script matches 10-digit phone numbers using regular expressions. It validates whether the input is a valid phone number.

**Example:**

```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
```

## 7. OMG WHY ARE YOU SHOUTING?

This script matches capital letters using a regular expression. It extracts capital letters from a given input string.

**Example:**

```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
```

These Ruby scripts and regular expressions cover various matching patterns and can be useful for tasks that involve pattern recognition and validation. Explore each script to understand how regular expressions work and how they can be applied in different scenarios.
