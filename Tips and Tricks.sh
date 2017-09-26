cat <file> | tr '\t' '|' | less -S ## replace '\t' with 'l'

## print records with a certain field length for each field
zcat <file> | cut -d'|' -f 5,6 | awk -F'|' '{if (length($1) > 2 && length($2) > 2) print}' | head

## sort by field
cat <file> | sort -t '|' -k 4 | less -S
