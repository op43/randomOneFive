Notes about my implementation:

	Part 1: only print out a random integer between 1 - 5 with the required frequencies

	Part 2: changed the function into a class which also stored the most recent 100 generated numbers

	Part 3: found an edge case when the history was empty and fixed it.(possible division by 0)
		wrote the most recent generated number into disk

	Part 4: changed the time value to datetime to be more precise with milliseconds
		added a new method writer which calls writeToDisk as a worker function
		writer runs on a single thread which writes the first object in a FIFO priority queue
		the FIFO queue ensures that the numbers / timestamps being written to disk will be in the correct order

	Part 5: created 5 threads running the generateRand() method which all insert the numbers/timestamps into the single writer thread