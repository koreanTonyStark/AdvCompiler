#!/bin/sh

for MODFILE in *.mod; do
	EXEFILE="${MODFILE%.mod}"
	if [ -e "$EXEFILE" ]; then
#		BASE="$(./"$EXEFILE")"
		echo "Running $EXEFILE"
		./"$EXEFILE"
		echo ""
	
		if [ -e "$EXEFILE.const" ]; then
			echo "Running $EXEFILE.const"
			./"$EXEFILE".const
			echo ""
#			CONST="$(./"$EXEFILE".const)"
#			if [ "$BASE" = "$CONST" ]; then
#				echo "$EXEFILE : constant propagation works"
#			fi
		fi

		if [ -e "$EXEFILE.const.dead" ]; then
			echo "Running $EXEFILE.const.dead"
			./"$EXEFILE".const.dead
			echo ""
#			DEAD="$(./"$EXEFILE".const.dead)"
#			if [ "$BASE" = "$DEAD" ]; then
#				echo "$EXEFILE : dead code elimination works"
#			fi
		fi
		echo ""
	fi
done
