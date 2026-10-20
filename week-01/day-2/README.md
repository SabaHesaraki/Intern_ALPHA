## Toolbox Task Note:
### Why did we put "$target" in Double Quotes?
If we don't use quotes and write just `$target`, Bash might split the path into separate words if there are any spaces in folder names (called word splitting). Putting it inside double quotes ensures Bash treats the whole path as a single solid string so `mkdir` and echo don't break.
