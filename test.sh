#!/bin/bash
#-----------------------------------------------------------
#
# validate mongo shell results using jq
#
#-----------------------------------------------------------
source mkSetup.sh

echo 'Performing a test comparing jq with similiar tool writen in python'

#
# test 1
#
echo
echo 'test1: compare count of json lines using jsonFetcher and jq'
echo 

python3 <<EOF
__doc__ = """
jq context:
jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log| wc -l 
-----------------------------------------------------------------------------------------------------------------------------
"""
print(__doc__)
EOF

jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log| wc -l 

python3 <<EOF
__doc__ = """
shell helper context:
cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | wc -l
-------------------------------------------------------------------------
"""
print(__doc__)
EOF

cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | wc -l

#
# test 2
#
echo
echo "test2: compare aggregating driver results"
echo ""

python3 <<EOF
__doc__ = """
jq context:
jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log | jq -cr '.attr.doc.driver' | grep -v null | sort | uniq -c | sort -rn
-----------------------------------------------------------------------------------------------------------------------------
"""
print(__doc__)
EOF

jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log | jq -cr '.attr.doc.driver' | grep -v null | sort | uniq -c | sort -rn

python3 <<EOF
__doc__ = """
shell helper context:
cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | drivers
-----------------------------------------------------------------------------------------------------------------------------
"""
print(__doc__)
EOF

cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | drivers

#
# test 3
#

echo
echo "test3: compare getting a count of queries taking the same "
echo ""

python3 <<EOF
__doc__ = """
jq context:
jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log | jq -c 'select(.attr.durationMillis>=2000)' |  wc -l
-----------------------------------------------------------------------------------------------------------------------------
"""
print(__doc__)
EOF

jq -c '. | select(.t["$date"] >= "2020-06-01T00:00:00.000" and .t["$date"] <= "2025-06-30T00:00:00.000")' mongodb.log | jq -c 'select(.attr.durationMillis>=2000)' |  wc -l

python3 <<EOF
__doc__ = """
shell helper context:
cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | millis -ge 2000 | wc -l
-----------------------------------------------------------------------------------------------------------------------------
"""
print(__doc__)
EOF

cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | millis -ge 2000 | wc -l