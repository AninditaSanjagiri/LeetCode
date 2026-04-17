<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?


<hr>

<h2>Approach: Hash Map (Dictionary)</h2>

<p>To solve this problem efficiently, we use a <strong>Hash Map</strong> to store numbers we have already visited along with their indexes.</p>

<p>For every number, we calculate its required complement:</p>

<pre>
complement = target - current_number
</pre>

<p>If that complement already exists in the dictionary, we immediately return both indexes.</p>

<p>This allows us to solve the problem in a single pass.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Create Hash Map</h3>

<pre>
seen = {}
</pre>

<p>This dictionary stores:</p>

<pre>
number : index
</pre>

<p>Example:</p>

<pre>
{
 2: 0,
 7: 1
}
</pre>

<p>Meaning:</p>

<ul>
    <li>Number <code>2</code> is at index <code>0</code></li>
    <li>Number <code>7</code> is at index <code>1</code></li>
</ul>

<hr>

<h3>Step 2: Traverse Array</h3>

<pre>
for i, num in enumerate(nums):
</pre>

<p>We go through the array one element at a time.</p>

<ul>
    <li><code>i</code> = current index</li>
    <li><code>num</code> = current number</li>
</ul>

<hr>

<h3>Step 3: Find Complement</h3>

<pre>
complement = target - num
</pre>

<p>This is the number needed to reach the target sum.</p>

<p>Example:</p>

<pre>
target = 9
num = 2

complement = 7
</pre>

<hr>

<h3>Step 4: Check If Complement Already Exists</h3>

<pre>
if complement in seen:
</pre>

<p>If yes, then we already found the matching pair earlier.</p>

<pre>
return [seen[complement], i]
</pre>

<p>Return:</p>

<ul>
    <li>Index of complement</li>
    <li>Current index</li>
</ul>

<hr>

<h3>Step 5: Store Current Number</h3>

<pre>
seen[num] = i
</pre>

<p>If no pair is found yet, store the current number and its index for future checks.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
nums = [2,7,11,15]
target = 9
</pre>

<table>
<tr>
<th>Index</th>
<th>Number</th>
<th>Complement</th>
<th>Hash Map</th>
<th>Action</th>
</tr>

<tr>
<td>0</td>
<td>2</td>
<td>7</td>
<td>{}</td>
<td>Store 2 → 0</td>
</tr>

<tr>
<td>1</td>
<td>7</td>
<td>2</td>
<td>{2:0}</td>
<td>Found pair → Return [0,1]</td>
</tr>
</table>

<p><strong>Output:</strong></p>

<pre>
[0,1]
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(n)</code></li>
</ul>

<hr>

<h2>Why This Is Optimal</h2>

<ul>
    <li>Single pass through array</li>
    <li>Constant time dictionary lookup</li>
    <li>No nested loops</li>
</ul>

<p>A brute force approach would take <code>O(n²)</code>, but this solution reduces it to <code>O(n)</code>.</p>

<hr>

<h2>Key Insight</h2>

<p>Instead of checking every pair, store previously seen numbers and instantly check whether the required complement already exists.</p>

<p>This makes the solution fast, clean, and interview-friendly.</p>
