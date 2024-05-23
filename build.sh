#!/bin/bash

mkdir docs

python3 chapters_split.py

npm run build

# Define the old and new titles with escaped special characters
old_title='<title data-rh="true">Nanosystems \| Nanosystems</title>'
new_title='<title data-rh="true">Nanosystems by K. Eric Drexler</title>'

# Define the old and new meta tags with escaped special characters
old_meta='<meta data-rh="true" property="og:title" content="Nanosystems \| Nanosystems">'
new_meta='<meta data-rh="true" property="og:title" content="Nanosystems by K. Eric Drexler">'

# Replace the title in the index.html file
sed -i "s|${old_title}|${new_title}|g" build/index.html

# Replace the meta tag in the index.html file
sed -i "s|${old_meta}|${new_meta}|g" build/index.html