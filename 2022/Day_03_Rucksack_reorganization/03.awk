#!/usr/bin/awk -f
# AdventOfCode 2022 -- Day 03: Rucksack Reorganization
# Fredrik Boulund 2022-12-03

function ord(char)
{
	return index(alphabet,char)
}

BEGIN {
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print "a priority is:", ord("a");
#print "A priority is:", ord("A");
sum_priorities=0;
line=0;
}


{
###### Part one
rucksacks=$0;

r_size=length($0)/2;
left=substr(rucksacks,0,r_size);
right=substr(rucksacks,r_size+1,r_size*2);

#print rucksacks, left, right;

for (i=1; i<=r_size; i++) {
	left_items[substr(left,i,1)]++;
	right_items[substr(right,i,1)]++;
}

for (l_item in left_items) {
	for (r_item in right_items) {
		if (l_item == r_item) {
			#print l_item;
			sum_priorities+=ord(l_item);
		}
	}

}

delete left_items;
delete right_items;

###### Part two
line++;
group[line % 3]=$0;
if (line % 3 == 0) {
	for (r in group) {
		rucksack=group[r];
		for (i=1; i<=length(rucksack); i++) {
			items[r][substr(rucksack,i,1)]++;
		}
	}
	for (r in group) {
		for (char in items[r]) {
			shared_counts[char]++;
		}
	}
	for (char in shared_counts) {
		if (shared_counts[char] == 3) {
			group_priorities+=ord(char);
		}
	}
	delete items;
	delete shared_counts;
}
}

END {
print sum_priorities;
print group_priorities;
}
