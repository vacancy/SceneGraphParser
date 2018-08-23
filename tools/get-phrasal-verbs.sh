#! /bin/sh
#
# get-phrasal-verbs.sh
# Copyright (C) 2018 Jiayuan Mao <maojiayuan@gmail.com>
#
# Distributed under terms of the MIT license.

set -x

rm -f ../sng_parser/_data/phrasal-verbs.txt

for alpha in {A..Z}
do
    echo curling $alpha
    curl \
        -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36" \
        http://www.english-for-students.com/Phrasal-Verbs-$alpha.html | python3 parse-eos.py >> ../sng_parser/_data/phrasal-verbs.txt
    sleep 3
done

