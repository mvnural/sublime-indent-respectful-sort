# About
Indent Respectful Sort is a Sublime Text plugin that provides sort functionality while respecting the block structure defined by indendation.

You may find this plugin useful when you have a consistently indented (all tabs or all 4 spaces etc.) file and would like to sort logical blocks (methods, classes or unordered lists) while maintaining inner structure of the blocks.

Note that this approach would only work in cases where indentation is not only present for readability but also for **dictating** the structure. 

# Usage
## Using predefined commands
Open command palette by typing `Ctrl + Shift + P` and start typing `IndentRespectulSort` to use one of the predefined sort options. 

As an example, running **Indent Respectful Sort: Indented by 2 Spaces & Max Depth = 2** command on the below snippet

    First Level Item 5
      Second Level Item 2
      Second Level Item 3
      Second Level Item 1
        Third Level Item 3
        Third Level Item 1
        Third Level Item 2
    First Level Item 2
      Second Level Item 2
        Third Level Item 2
        Third Level Item 1
      Second Level Item 1
      
would yield the following.

    First Level Item 2
      Second Level Item 1
      Second Level Item 2
        Third Level Item 2
        Third Level Item 1
    First Level Item 5
      Second Level Item 1
        Third Level Item 3
        Third Level Item 1
        Third Level Item 2
      Second Level Item 2
      Second Level Item 3

## Running a custom sort command
You may run `IndentRespectfulSort` directly from the console if you need custom sort options.

1.  Open the Python console by pressing ``Ctrl+` `` or by selecting View | Show Console in the menu.
2.  Type `view.run_command("indent_respectful_sort")` and hit `Enter` to run `IndentRespectfulSort` with default options (tab delimited).
3.  You may specify arguments in the second parameter of the run command. Eg. `view.run_command("indent_respectful_sort", {"indent": "  ", "maxDepth": 2})`

### Args
- *maxDepth*: Do not sort blocks beyond levels specified by this argument. (default: unlimited)
- *onlyDepth*: Only sort the blocks in the level specified by this argument. If *onlyDepth* is specified, then *maxDepth* is ignored. (default: None)
- *indent*: Specify the indentation used in this file. (default: "\t")

# Installation
## Using Package Control
IndentRespectfulSort can easily be installed via Package Control. 

1. Make sure Package Control is installed. (See https://packagecontrol.io/installation).
2. Press `ctrl + shift + p `(Win, Linux) or `cmd + shift + p` (OSX) to open command palette. Find and select `Package Control : Install Package` and hit `Enter`.
3. In the newly opened panel, start typing `IndentRespectfulSort` and hit `Enter` after you have found and selected.
4. Done!

## Manual Installation
1. Create a folder named `IndentRespectfulSort` in the sublime packages folder.
2. Simply extract the contents of this repository into the newly created `IndentRespectfulSort` folder.

# Statistics
Available on the Package Control website. See https://packagecontrol.io/packages/Indent%20Respectful%20Sort

# Bugs / Feature Requests
You may create a new issue at https://github.com/mvnural/sublime-indent-respectful-sort/issues 
