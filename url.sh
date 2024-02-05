#!/bin/bash

# 设置 CDN 前缀
cdn_prefix="https://cdn.jsdelivr.net/gh/bgvioletsky/testaction"

find . -type f -iname "*.jpg" | awk 'length($0) >= 13' | jq --arg prefix "$cdn_prefix" -R -s  '[split("\n")[] | select(. != "") | sub("^\\."; "") | $prefix + .]' > img_url.json
find . -type f -iname "*.jpg" -exec basename {} \; | awk 'length($0) >= 13'| jq -R -s '[split("\n")[] | select(. != "") ]'  >img_name.json
find . -type f -name "*.jpg" -exec sh -c 'mkdir -p "$(dirname "{}")" && echo "{ \"url\": \"$(basename "{}")\" }" > "$(dirname "{}")/urlk.json"' \;
