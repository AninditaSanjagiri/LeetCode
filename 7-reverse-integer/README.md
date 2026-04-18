<h2><a href="https://leetcode.com/problems/reverse-integer">Reverse Integer</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


<hr>

<h2>Approach: Mathematical Digit Reversal</h2>

<p>Instead of converting the integer into a string, we reverse the number mathematically using modulus and division.</p>

<p>For each step:</p>

<ul>
    <li>Take the last digit using <code>% 10</code></li>
    <li>Remove the last digit using <code>// 10</code></li>
    <li>Append the digit to the reversed number</li>
</ul>

<p>This continues until all digits are processed.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def reverse(self, x: int) -&gt; int:

        sign = -1 if x &lt; 0 else 1
        x = abs(x)

        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        reversed_num *= sign

        if reversed_num &lt; -2**31 or reversed_num &gt; 2**31 - 1:
            return 0

        return reversed_num
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Store Sign</h3>

<pre>
sign = -1 if x &lt; 0 else 1
</pre>

<p>If the number is negative, store <code>-1</code>. Otherwise store <code>1</code>.</p>

<p>This lets us work with a positive number first, then restore the sign later.</p>

<hr>

<h3>Step 2: Convert to Positive</h3>

<pre>
x = abs(x)
</pre>

<p>Examples:</p>

<pre>
123  → 123
-123 → 123
</pre>

<p>This avoids Python negative division issues.</p>

<hr>

<h3>Step 3: Initialize Result</h3>

<pre>
reversed_num = 0
</pre>

<p>This will store the reversed integer as we build it digit by digit.</p>

<hr>

<h3>Step 4: Extract Last Digit</h3>

<pre>
digit = x % 10
</pre>

<p>This gives the last digit.</p>

<p>Example:</p>

<pre>
123 % 10 = 3
</pre>

<hr>

<h3>Step 5: Append Digit to Result</h3>

<pre>
reversed_num = reversed_num * 10 + digit
</pre>

<p>Example:</p>

<pre>
reversed_num = 0
digit = 3

0 * 10 + 3 = 3
</pre>

<p>Next step:</p>

<pre>
3 * 10 + 2 = 32
</pre>

<p>Then:</p>

<pre>
32 * 10 + 1 = 321
</pre>

<hr>

<h3>Step 6: Remove Last Digit from x</h3>

<pre>
x = x // 10
</pre>

<p>This removes the last digit.</p>

<p>Examples:</p>

<pre>
123 // 10 = 12
12 // 10 = 1
1 // 10 = 0
</pre>

<hr>

<h3>Step 7: Restore Sign</h3>

<pre>
reversed_num *= sign
</pre>

<p>If original number was negative:</p>

<pre>
321 → -321
</pre>

<hr>

<h3>Step 8: Check 32-bit Overflow</h3>

<pre>
if reversed_num &lt; -2**31 or reversed_num &gt; 2**31 - 1:
    return 0
</pre>

<p>Valid signed 32-bit range:</p>

<pre>
-2147483648 to 2147483647
</pre>

<p>If reversed number exceeds this range, return <code>0</code>.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
x = 123
</pre>

<table>
<tr>
<th>x</th>
<th>digit</th>
<th>reversed_num</th>
</tr>

<tr>
<td>123</td>
<td>3</td>
<td>3</td>
</tr>

<tr>
<td>12</td>
<td>2</td>
<td>32</td>
</tr>

<tr>
<td>1</td>
<td>1</td>
<td>321</td>
</tr>

<tr>
<td>0</td>
<td>-</td>
<td>Stop</td>
</tr>
</table>

<p><strong>Output:</strong></p>

<pre>
321
</pre>

<hr>

<h2>Example with Negative Number</h2>

<pre>
x = -120
</pre>

<p>Reverse digits:</p>

<pre>
021 → 21
</pre>

<p>Restore sign:</p>

<pre>
-21
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(log₁₀ n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<p>We process one digit at a time.</p>

<hr>

<h2>Why This Is Efficient</h2>

<ul>
    <li>No string conversion required</li>
    <li>Constant extra space</li>
    <li>Works digit by digit</li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>Use modulo to extract the last digit, integer division to remove it, and rebuild the reversed number step by step.</p>
