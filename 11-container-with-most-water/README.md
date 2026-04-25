<h2><a href="https://leetcode.com/problems/container-with-most-water">Container With Most Water</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>




<hr>

<h2>Approach: Two Pointers</h2>

<p>We need to choose two vertical lines that can hold the maximum amount of water.</p>

<p>The water area formed between two lines depends on:</p>

<pre>
Area = Width × Height
</pre>

<p>Where:</p>

<ul>
    <li><strong>Width</strong> = distance between the two lines</li>
    <li><strong>Height</strong> = smaller of the two lines</li>
</ul>

<pre>
Area = (right - left) × min(height[left], height[right])
</pre>

<p>Instead of checking every pair using brute force <code>O(n²)</code>, we use two pointers to solve it in linear time.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def maxArea(self, height: List[int]) -&gt; int:

        left = 0
        right = len(height) - 1
        max_water = 0

        while left &lt; right:

            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_water = max(max_water, area)

            if height[left] &lt; height[right]:
                left += 1
            else:
                right -= 1

        return max_water
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Initialize Two Pointers</h3>

<pre>
left = 0
right = len(height) - 1
</pre>

<p>Start with the widest possible container:</p>

<ul>
    <li><code>left</code> at first index</li>
    <li><code>right</code> at last index</li>
</ul>

<hr>

<h3>Step 2: Calculate Width</h3>

<pre>
width = right - left
</pre>

<p>This is the horizontal distance between two lines.</p>

<hr>

<h3>Step 3: Calculate Height</h3>

<pre>
current_height = min(height[left], height[right])
</pre>

<p>Water level is limited by the shorter line.</p>

<p>Example:</p>

<pre>
8 and 7 → water height = 7
</pre>

<hr>

<h3>Step 4: Calculate Area</h3>

<pre>
area = width * current_height
</pre>

<hr>

<h3>Step 5: Update Maximum Area</h3>

<pre>
max_water = max(max_water, area)
</pre>

<p>Store best result found so far.</p>

<hr>

<h3>Step 6: Move the Shorter Pointer</h3>

<pre>
if height[left] &lt; height[right]:
    left += 1
else:
    right -= 1
</pre>

<p>This is the key optimization.</p>

<p>Why?</p>

<ul>
    <li>Width always decreases after moving a pointer</li>
    <li>To possibly get larger area, we need a taller shorter side</li>
    <li>So move the smaller height inward</li>
</ul>

<p>Moving the taller line cannot help because the shorter line still limits height.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
height = [1,8,6,2,5,4,8,3,7]
</pre>

<h3>Initial State</h3>

<pre>
left = 0 (1)
right = 8 (7)
</pre>

<p>Area:</p>

<pre>
width = 8
height = min(1,7) = 1
area = 8
</pre>

<p>Move left pointer because 1 is smaller.</p>

<hr>

<h3>Next State</h3>

<pre>
left = 1 (8)
right = 8 (7)
</pre>

<p>Area:</p>

<pre>
width = 7
height = min(8,7) = 7
area = 49
</pre>

<p>Maximum becomes:</p>

<pre>
49
</pre>

<p>This is the final answer.</p>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<p>Each pointer moves inward at most once per index.</p>

<hr>

<h2>Why This Is Optimal</h2>

<ul>
    <li>No nested loops</li>
    <li>Each height processed efficiently</li>
    <li>Impossible pairs are eliminated logically</li>
</ul>

<p>Brute force takes <code>O(n²)</code>, but this solution reduces it to <code>O(n)</code>.</p>

<hr>

<h2>Key Insight</h2>

<p>The shorter line always limits water height.</p>

<p>So after checking an area, discard the shorter side and search for a taller one.</p>
