"""----------------------------------------------------------------------------------------------------------------------------------------------------
This was a challenge I solved in 2019. The orginal posting is here - https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/

I included this to show knowledge of python, unittesting and problem solving

The script needs to be run in python3. It was written in 3.6.5
----------------------------------------------------------------------------------------------------------------------------------------------------- """


"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4

    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2

    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].



"""
import unittest
import math

def solution(A):
    """
    Given a non-empty array A consisting of N integers this function returns the maximum number of blocks into which A can be divided.

    Args:
        A (array): a non-empty array of integers in the range [1...100,000]

    Returns:
        (integer): the maximum number of blocks into which A can be divided

    """
    peaks = find_peaks(A)
    factors = find_common_factors(len(A))
    for factor in factors:
        works = check_against_divisor(peaks,factor)
        if works:
            return int(len(A) / factor)
    return 0

def find_peaks(A):
    """
    This function finds all of the peaks in array A and returns another array where the peaks are represented by 1's and the non-peaks by zero's

        Args:
            A (array): a non-empty array of integers in the range [1...100,000]

        Returns:
            (array) : an array the same length as A of zero's and one's showing the peaks

    """


    peaks = [0]
    for i in range(1,len(A)-1):
        previous, current, next = A[i-1],A[i],A[i+1]
        if previous < current > next:
            peaks.append(1)
        else:
            peaks.append(0)
    peaks.append(0)
    return peaks

def find_common_factors(n):
    """
    This function finds all of the common factors in integer n

    Args:
        n (integer): a non-negative integer

    Returns:
        (integer) : the number of factors in n

    """

    sq = int(math.sqrt(n))
    factors = []
    for i in range(1,sq+1):
        if n % i == 0:
            factors.extend([int(n/i),i])

    return sorted(list(set(factors)),reverse=False)

def check_against_divisor(peaks,chunk_size):
    """
    This function checks whether the list of peaks, when split into chunks of length 'chunk_size' has a peak in each chunk

    Args:
        peaks (array): an array where peaks are represented by 1's and non-peaks by 0's

    Returns:
        (boolean) : whether every chunk contains a peak

    """

    for i in range(0,len(peaks),chunk_size):
        chunk = peaks[i:i+chunk_size]
        if sum(chunk) == 0:
            return False
    return True

class Test_Peaks(unittest.TestCase):

    def setUp(self):
        self.A = [1,2,3,4,3,4,1,2,3,4,6,2]
        self.B = [6,5,6,4,4,1,2,3,4,5,6,1]
        self.C = [5]
        self.D = [1,5,1]
        self.E = [7, 1, 2,1, 3,6,1,1]

    def test_find_peaks(self):
        res = [0,0,0,1,0,1,0,0,0,0,1,0]
        self.assertEqual(find_peaks(self.A),res)
        res2 = [0,0,0,1,0,1,0,0,0,0,0,0]
        one_at_end= [1,2,3,4,3,4,1,2,3,4,6,20]
        self.assertEqual(find_peaks(one_at_end),res2)

    def test_common_factors(self):
        self.assertEqual(find_common_factors(12),sorted([12,6,4,3,2,1],reverse=False))
        self.assertEqual(find_common_factors(1),[1])
        self.assertEqual(find_common_factors(13),[1,13])
        self.assertEqual(find_common_factors(8),sorted([8,4,2,1],reverse=False))

    def test_check_against_divisor(self):
        peaks = find_peaks(self.A)
        self.assertFalse(check_against_divisor(peaks,2))
        self.assertFalse(check_against_divisor(peaks,3))
        self.assertTrue(check_against_divisor(peaks, 4))

    def test_check_against_divisor2(self):

        peaks2= [0,1,0,0,0,1,1,0,0]
        self.assertTrue(check_against_divisor(peaks2,3))
        self.assertFalse(check_against_divisor(peaks2,4))
        peaks3 = [0]
        self.assertFalse(check_against_divisor(peaks3,2))

    def test_given(self):
        self.assertEqual(solution(self.A),3)
        self.assertEqual(solution(self.B),2)
        self.assertEqual(solution(self.C),0)

        self.assertEqual(solution(self.D),1)
        self.assertEqual(solution(self.E),2)

if __name__ == "__main__":
    unittest.main()











