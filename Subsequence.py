Validate Subsequence

Given two non-empty arrays of integers. write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear
in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that 
a single number in an array and the array itself are both valid subsequences of the array.

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

The algorythm has to traverse both arrays and check if the elements of the sequence are present in order in the array and then it can stop 
once the elements of the sequence are met. 

Time complexity will be O(N) where N is the length of the main array.

Space complexity will be constant so O(1) because we aren't storing anything extra or will increase in size.


arrIdx = 0
seqIdx = 0

#while our array index is less than the length of the array
#and while our sequence index is less than the length of the sequence
#we are looking to see if the element we are in the array is the same
#as the element in the sequence and regardless if its a match or not
#we are going to increment the array by 1
#we will only have a valid subsequence if the sequence index is smaller
#than the length of the sequence

# O(n) time O(1) space
def validateSebsequence(array, sequence):
    
arrIdx = 0
seqIdx = 0

while arrIdx < len(array) and seqIdx < len(sequnece):
    if array[arrIdx] == sequence[seqIdx]:
        seqIdx += 1
    arrIdx += 1
return seqIdx == len(sequence)


#done with a for loop

def validateSebsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value"
        seqIdx +=1
    return seqIdx == len(sequence)


My Solution Code:

function isValidSubsequence(array, sequence) {

	let seqIdx = 0;
	for (const value of array){
		if (seqIdx == sequence.length);
		if (sequence[seqIdx] == value)
			seqIdx +=1;
	}
    return seqIdx == sequence.length;
}


exports.isValidSubsequence = isValidSubsequence;