<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">Median of Two Sorted Arrays</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>


<hr>

<h2>Approach: Binary Search Partition</h2>

<p>This problem asks for the median of two already sorted arrays.</p>

<p>A direct merge solution works in <code>O(m+n)</code>, but the optimal solution uses <strong>Binary Search</strong> and runs in:</p>

<pre>
O(log(min(m,n)))
</pre>

<p>Instead of merging arrays, we partition both arrays into left and right halves such that:</p>

<ul>
    <li>Total elements on left side = half of all elements</li>
    <li>Every left-side value ≤ every right-side value</li>
</ul>

<p>Once that partition is found, the median can be calculated instantly.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left &lt;= right:

            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            r1 = float('inf') if cut1 == m else nums1[cut1]

            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r2 = float('inf') if cut2 == n else nums2[cut2]

            if l1 &lt;= r2 and l2 &lt;= r1:

                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            elif l1 &gt; r2:
                right = cut1 - 1

            else:
                left = cut1 + 1
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Binary Search the Smaller Array</h3>

<pre>
if len(nums1) &gt; len(nums2):
    nums1, nums2 = nums2, nums1
</pre>

<p>We always search the smaller array to minimize binary search time.</p>

<hr>

<h3>Step 2: Partition Both Arrays</h3>

<pre>
cut1 = (left + right) // 2
cut2 = (m + n + 1) // 2 - cut1
</pre>

<p>If <code>cut1</code> elements are taken from <code>nums1</code> into the left half, then <code>cut2</code> must come from <code>nums2</code>.</p>

<p>This ensures left side always contains half of total elements.</p>

<hr>

<h3>Step 3: Get Border Values</h3>

<p>We only care about values near the partition.</p>

<pre>
l1 = largest value on left side of nums1
r1 = smallest value on right side of nums1

l2 = largest value on left side of nums2
r2 = smallest value on right side of nums2
</pre>

<p>These four values determine whether partition is valid.</p>

<hr>

<h3>Step 4: Check Valid Partition</h3>

<pre>
if l1 &lt;= r2 and l2 &lt;= r1
</pre>

<p>This means:</p>

<ul>
    <li>All left-half values are smaller than right-half values</li>
    <li>Correct split has been found</li>
</ul>

<hr>

<h3>Step 5: Calculate Median</h3>

<h4>If Total Length is Odd</h4>

<pre>
return max(l1, l2)
</pre>

<p>The left half contains one extra middle element.</p>

<h4>If Total Length is Even</h4>

<pre>
return (max(l1,l2) + min(r1,r2)) / 2
</pre>

<p>Median is average of two middle values.</p>

<hr>

<h3>Step 6: If Partition Is Wrong</h3>

<h4>Case 1: Too Many Elements Taken from nums1</h4>

<pre>
l1 &gt; r2
</pre>

<p>Move left:</p>

<pre>
right = cut1 - 1
</pre>

<h4>Case 2: Too Few Elements Taken from nums1</h4>

<p>Move right:</p>

<pre>
left = cut1 + 1
</pre>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
nums1 = [1,3]
nums2 = [2]
</pre>

<p>After ensuring smaller array first:</p>

<pre>
nums1 = [2]
nums2 = [1,3]
</pre>

<p>Try partition:</p>

<pre>
nums1 = [2 | ]
nums2 = [1 | 3]
</pre>

<p>Left side:</p>

<pre>
[2,1]
</pre>

<p>Right side:</p>

<pre>
[3]
</pre>

<p>Border values:</p>

<pre>
l1 = 2
r1 = inf
l2 = 1
r2 = 3
</pre>

<p>Check:</p>

<pre>
2 &lt;= 3   ✔
1 &lt;= inf ✔
</pre>

<p>Valid partition found.</p>

<p>Total length is odd, so:</p>

<pre>
median = max(2,1) = 2
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(log(min(m,n)))</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<hr>

<h2>Why This Is Optimal</h2>

<ul>
    <li>No merging required</li>
    <li>No sorting required</li>
    <li>Uses binary search on smaller array only</li>
    <li>Reads only partition boundary values</li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>The median depends only on the correct split between left and right halves, not on fully merging both arrays.</p>

<p>Find the split using binary search, then compute the answer directly.</p>
