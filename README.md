# Majority-Element
solution in Python , JS

When we start, we arbitrarily pick the first element as our candidate and set `count = 1`. This essentially means "I have seen this number once".

As we move forward in the array:

1. If we see the same number again (`num == candidate`), we increase the count by 1. This means "My belief that this is the majority element has strengthened."

2. If we see a different number (`num != candidate`), we decrease the count by 1. This effectively means "My belief that this is the majority element has weakened."

Now, if the `count` ever reaches 0, it means our initial choice for the candidate might not be the majority element, because we have seen an equal number of occurrences of the candidate and some other numbers. This makes our current candidate invalid, so we choose the next number we see as our new candidate and start the count for it.

Here's a walkthrough using the array `[2, 2, 1, 1, 1, 2, 2]`:

1. Candidate = 2, Count = 1 (Starting with the first element)
2. See another 2: Candidate = 2, Count = 2
3. See 1 (different from candidate): Candidate = 2, Count = 1
4. See another 1: Candidate = 2, Count = 0
5. At this point, the count is 0, so the next number we see, which is 1, will be our new candidate. Candidate = 1, Count = 1
6. See another 1: Candidate = 1, Count = 2
7. See 2 (different from candidate): Candidate = 1, Count = 1
8. See another 2: Candidate = 1, Count = 0

By the end of the loop, the candidate is 1 with count 0. But then, we see another 2 right after that, and since the count is 0, this new 2 becomes the candidate. This happens outside of the loop logic as the loop completes its iteration.

This method leverages the fact that the majority element occurs more than n/2 times. So, it will always end up as the candidate by the time you've processed the entire list, even if the count is not greater than 0 at that exact moment.
