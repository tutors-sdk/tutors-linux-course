mkdir html && grep Prof names.txt | while read -r line; do echo "<h1>${line}</h1><p>content...</p>" > "html/$(echo "$line" | awk '{print $2 $3}').html"; done
