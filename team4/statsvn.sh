#!/bin/sh

LOGFILE=logfile.log
STATDIR=./stats
STATSVNDIR=/usr/share/java
INCLUDES="**/*.cpp;**/*.h;**/Makefile;**/*.mod"
EXCLUDES=""

#Creating an SVN log file
if [ -f "$LOGFILE" ]; then
	rm -f "$LOGFILE"
fi

svn log -v --xml > "$LOGFILE"

#Running StatSVN
if [ -d "$STATDIR" ]; then
	rm -rf "$STATDIR"
fi

java -jar "$STATSVNDIR"/statsvn.jar -verbose -include "$INCLUDES" -exclude "$EXCLUDES" -output-dir "$STATDIR" ./"$LOGFILE" .
