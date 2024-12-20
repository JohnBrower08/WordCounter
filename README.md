# WordCounter
## Program outline
Python Program Assignment:

    Create a Python program called “WordCounter.py” that has two arguments:
        Input file – this will be a .txt file that will have a small story in it consisting of multiple lines.
        Output file – this will be a .csv file that will consist of the following information:
            Column 1 (key) – the word that was found in the input file.
            Column 2 (value) – the total number of times that the word appeared in the input file. 
    The python file will review the arguments and provide an appropriate error message if not correct. 
        Examples:
            Error message if “no” input file or output file are listed.
            Error message if input file does not have the extension “.txt”
            Error message if output file does not have the extension “.csv”
            Error message if there are more than three arguments listed on the command line. 
    The python file will attempt to open the input file and read in everything in the file on a line-by-line basis.
        If the file does not exist, there should be an error message.
        If the file can be read, the program will read in line-by-line each line in the file.
        The data in the line will be parsed to identify each word
        The program will keep count of how many times it finds each unique word in the file. 
        The program can ignore white space like tabs
        The program will ignore the following punctuation such as “,” “.”, “!”, “?”
        Numbers such as “23” can be considered a “word” (just to make it easier). 
        If there is a problem reading the data (such as opening a binary file instead of a text file, or the file is just empty), then the program should catch the error and display an appropriate error message.  
    When the program is done, the program will display the following on the screen:
        The word (or words) that appear the most in the file and how many times it appeared. 
    When the program is done, the program will save the data collected with the words and the number of times it occurred into the output.csv file.
        If the output file does not exist, the program will create it.
        If the output file does exist, the program file will overwrite it.  
        If the output .csv file cannot be written to (because it is open from a previous run as an example), the program should provide an error message stating there was an error.
        The file should list the words in alphabetical order.

## How to use