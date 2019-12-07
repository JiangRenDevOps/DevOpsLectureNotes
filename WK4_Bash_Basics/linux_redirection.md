# Redirection
Most processes initiated by UNIX commands write to the standard output (that is, they write to the terminal screen), and many take their input from the standard input (that is, they read it from the keyboard). There is also the standard error, where processes write their error messages, by default, to the terminal screen.



```
cat list1
```
We use the `>` symbol to redirect the output of a command. 
```
cat > list1
```
Please type anything, press enter

```
cp list1 list2
```
The form `>>` appends standard output to a file
```
cat >> list1
```
Please type anything, press `enter` and check list1

Now, you should have list1 and list2

Please type 
```
cat list1 list2 > list3
```
and now you should have a new list, check what is in there:
```
cat list3
```

Let us sort it. Using `<` you can redirect the input to come from a file rather than the keyboard
```
sort < list3
```

What does this do? 

```
sort < list3 > slist3
```
`|` pipe the output of command1 to the input of command2
```
who | sort
```