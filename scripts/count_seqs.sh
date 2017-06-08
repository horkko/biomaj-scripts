#! /bin/sh

# This script is intented to count the number of sequence(s) from a file
# It supports format supported by squizz

root=/pasteur/services/banques/biomaj3
bin="$root/bin"
trash="/tmp/$$.biomaj-trash"

test -d ${root} || { echo "$root not found: $!" && exit 1; }
# Args: <format> <file>
# Format
fmt=$1
shift
file=$1
shift
# Default to FASTA format
delim='^>'

if test -z "$dbname"; then
    echo "Can't count sequence, \$dbname not set";
    exit 1;
fi

if test -z "$fmt" || test -z "$file"; then
    echo "Option(s) missing"
    echo "update_sequence_count.sh <format> <file>"
    exit 1;
fi

if [ "$fmt" = "FASTA" ]; then
    delim='^>'
elif [ "$fmt" = "EMBL" ]; then
    delim=""
elif [ "$fmt" = "GENBANK"]; then
    delim="^LOCUS"
else
    echo ">&2 Unsupported format $fmt"
    exit 1;
fi

trap 'rm -rf $trash' EXIT

nsq=$(grep -c "$delim" $file 2> $trash)
if [ "$?" != 0 ]; then
    cat $trash
    exit 1
fi

test -z $nsq && {echo "Can't get sequence number from file $file" && exit 1; }

# Activate virtualenv
source $bin/activate

dblen=$(expr length "${dbname}_")
dblen=$(expr $dblen + 1)
release=$(echo $localrelease | cut -c $dblen- )

res=$(biomaj-manager.py -b $dbname --set_sequence_count $file:$nsq -r $release)

if [ "$?" != 0 ]; then
    echo "Can't set sequence count: $res"
    deactivate
    exit 1;
fi

deactivate

exit 0