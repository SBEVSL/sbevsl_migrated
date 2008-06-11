The batch motifer is a tool that checks your molecules of interest for known
motifs at different levels of sensitivity. What makes it different from the
other motif tool is its ability to check a list of molecules, it then outputs an
easy to read textfile that can be read as a spreadsheet for easy parsing.

Here's how you use it:

1.) Since you've already installed ProMOL go ahead and start it up and click on
the batch motif tab.

2.) Now in the Sentivities textbox, you can give a list of sentivities at which
test your molecules. The sensitivites range from any number between 0 and 2. You
must list seperated by commas. Example: .5,1,1.2,1.5

3.) The click browse to find your txt file of pdb codes each having their own
line. The file should look something like this:

1TIM
3YPI
1AH2
1BEA

...and so on.

4.) Click run, this will then ask you where to save the output file.

5.) If everything is fine, the algorithm will run fine, otherwise, a message
will pop up to tell you how to correct any mistakes you might have made

6.) The output should be a .motif file. It is really just a text file, but since
the out put is tab delimited you can have .motif files specifically opened by
spreadsheet programs.
