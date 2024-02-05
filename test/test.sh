find . -type f -name "*.jpg" -exec sh -c 'mkdir -p "$(dirname "{}")" && echo "{ \"url\": \"$(basename "{}")\" }" > "$(dirname "{}")/urlk.json"' \;

find . -type f -name "*.jpg" -exec sh -c 'dir=$(dirname "{}"); echo "{ \"files\": [" > "$dir/url.json" && find "$dir" -maxdepth 1 -type f -name "*.jpg" -exec basename {} \; | sed -e :a -e N -e '$!ba' -e 's/\n/, /g' >> "$dir/url.json" && echo -e "\n]" >> "$dir/url.json"' \;
