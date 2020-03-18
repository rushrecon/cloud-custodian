bazel test $1 | perl -pe 's/.*(?<!\.log)$//' | while read line; do if [[ $line =~ \.log$ ]]; then echo $line; cat $line; fi; done
