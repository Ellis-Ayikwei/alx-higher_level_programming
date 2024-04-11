# Curriculum

## SE Foundations
- **Average:** 73.43%
- Advanced tasks released.

## 0x13. JavaScript - Objects, Scopes and Closures
### JavaScript
- **Weight:** 1
- Ongoing second chance project - started Apr 9, 2024 6:00 AM, must end by Apr 12, 2024 6:00 AM
- An auto review will be launched at the deadline

#### In a nutshell…
- Auto QA review: 0.0/116 mandatory & 0.0/29 optional
- Altogether: 0.0%
- Mandatory: 0.0%
- Optional: 0.0%
- Calculation: 0.0% + (0.0% * 0.0%) == 0.0%

#### Resources
- Read or watch:
  - [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
  - [Object-oriented JavaScript (read all examples!)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
  - [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
  - [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
  - [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
  - [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
  - [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
  - [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
  - [this/self](https://alistapart.com/article/getoutbindingsituations/)
  - [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

#### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- **General:**
  - Why JavaScript programming is amazing
  - How to create an object in JavaScript
  - What `this` means
  - What `undefined` means
  - Why the variable type and scope is important
  - What is a closure
  - What is a prototype
  - How to inherit an object from another

#### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

#### Requirements
- **General:**
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/node`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
  - All your files must be executable
  - The length of your files will be tested using `wc`
  - You are not allowed to use `var`

#### More Info
- **Install Node 14**
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs





  # JavaScript Objects, Scopes and Closures Tasks

## Table of Contents
1. [Rectangle #0](#rectangle-0)
2. [Rectangle #1](#rectangle-1)
3. [Rectangle #2](#rectangle-2)
4. [Rectangle #3](#rectangle-3)
5. [Rectangle #4](#rectangle-4)
6. [Square #0](#square-0)
7. [Square #1](#square-1)
8. [Occurrences](#occurrences)
9. [Esrever](#esrever)
10. [Log Me](#log-me)
11. [Number Conversion](#number-conversion)
12. [Factor Index](#factor-index)
13. [Sorted Occurrences](#sorted-occurrences)
14. [Concat Files](#concat-files)

## Tasks

### Rectangle #0
- Write an empty class `Rectangle` that defines a rectangle.
  - Use the class notation for defining your class.

### Rectangle #1
- Write a class `Rectangle` that defines a rectangle.
  - Use the class notation for defining your class.
  - The constructor must take 2 arguments `w` and `h`.
  - Initialize the instance attribute `width` with the value of `w`.
  - Initialize the instance attribute `height` with the value of `h`.

### Rectangle #2
- Write a class `Rectangle` that defines a rectangle.
  - Use the class notation for defining your class.
  - The constructor must take 2 arguments `w` and `h`.
  - Initialize the instance attribute `width` with the value of `w`.
  - Initialize the instance attribute `height` with the value of `h`.
  - If `w` or `h` is equal to 0 or not a positive integer, create an empty object.

### Rectangle #3
- Write a class `Rectangle` that defines a rectangle.
  - Use the class notation for defining your class.
  - The constructor must take 2 arguments: `w` and `h`.
  - Initialize the instance attribute `width` with the value of `w`.
  - Initialize the instance attribute `height` with the value of `h`.
  - If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
  - Create an instance method called `print()` that prints the rectangle using the character `X`.

### Rectangle #4
- Write a class `Rectangle` that defines a rectangle.
  - Use the class notation for defining your class.
  - The constructor must take 2 arguments: `w` and `h`.
  - Initialize the instance attribute `width` with the value of `w`.
  - Initialize the instance attribute `height` with the value of `h`.
  - If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
  - Create an instance method called `print()` that prints the rectangle using the character `X`.
  - Create an instance method called `rotate()` that exchanges the width and the height of the rectangle.
  - Create an instance method called `double()` that multiplies the width and the height of the rectangle by 2.

### Square #0
- Write a class `Square` that defines a square and inherits from `Rectangle`.
  - Use the class notation for defining your class and `extends`.
  - The constructor must take 1 argument: `size`.
  - The constructor of `Rectangle` must be called (by using `super()`).

### Square #1
- Write a class `Square` that defines a square and inherits from `Square`.
  - Use the class notation for defining your class and `extends`.
  - Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`.
  - If `c` is undefined, use the character `X`.

### Occurrences
- Write a function that returns the number of occurrences in a list.
  - Prototype: `exports.nbOccurences = function (list, searchElement)`.

### Esrever
- Write a function that returns the reversed version of a list.
  - Prototype: `exports.esrever = function (list)`.
  - You are not allowed to use the built-in method `reverse`.

### Log Me
- Write a function that prints the number of arguments already printed and the new argument value.
  - Prototype: `exports.logMe = function (item)`.
  - Output format: `<number arguments already printed>: <current argument value>`.

### Number Conversion
- Write a function that converts a number from base 10 to another base passed as an argument.
  - Prototype: `exports.converter = function (base)`.
  - You are not allowed to import any file.
  - You are not allowed to declare any new variable (`var`, `let`, etc.).

### Factor Index
- Write a script that imports an array and computes a new array.
  - Your script must import `list` from the file `100-data.js`.
  - You must use a map.
  - A new list must be created with each value equal to the value of the initial list, multiplied by the index in the list.
  - Print both the initial list and the new list.

### Sorted Occurrences
- Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
  - Your script must import `dict` from the file `101-data.js`.
  - In the new dictionary:
    - A key is a number of occurrences.
    - A value is the list of user ids.
  - Print the new dictionary at the end.

### Concat Files
- Write a script that concatenates 2 files.
  - The first argument is the file path of the first source file.
  - The second argument is the file path of the second source file.
  - The third argument is the file path of the destination.


