<h2><a href="https://leetcode.com/problems/string-to-integer-atoi">String to Integer (atoi)</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Implement the <code>myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer.</p>

<p>The algorithm for <code>myAtoi(string s)</code> is as follows:</p>

<ol>
	<li><strong>Whitespace</strong>: Ignore any leading whitespace (<code>&quot; &quot;</code>).</li>
	<li><strong>Signedness</strong>: Determine the sign by checking if the next character is <code>&#39;-&#39;</code> or <code>&#39;+&#39;</code>, assuming positivity if neither present.</li>
	<li><strong>Conversion</strong>: Read the integer by skipping leading zeros&nbsp;until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.</li>
	<li><strong>Rounding</strong>: If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then round the integer to remain in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be rounded to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be rounded to <code>2<sup>31</sup> - 1</code>.</li>
</ol>

<p>Return the integer as the final result.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;42&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
The underlined characters are what is read in and the caret is the current reader position.
Step 1: &quot;42&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;42&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>42</u>&quot; (&quot;42&quot; is read in)
           ^
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot; -042&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;<u>   </u>-042&quot; (leading whitespace is read and ignored)
            ^
Step 2: &quot;   <u>-</u>042&quot; (&#39;-&#39; is read, so the result should be negative)
             ^
Step 3: &quot;   -<u>042</u>&quot; (&quot;042&quot; is read in, leading zeros ignored in the result)
               ^
</pre>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1337c0d3&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1337</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;1337c0d3&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;1337c0d3&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>1337</u>c0d3&quot; (&quot;1337&quot; is read in; reading stops because the next character is a non-digit)
             ^
</pre>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0-1&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: &quot;0-1&quot; (no characters read because there is no leading whitespace)
         ^
Step 2: &quot;0-1&quot; (no characters read because there is neither a &#39;-&#39; nor &#39;+&#39;)
         ^
Step 3: &quot;<u>0</u>-1&quot; (&quot;0&quot; is read in; reading stops because the next character is a non-digit)
          ^
</pre>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;words and 987&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Reading stops at the first non-digit character &#39;w&#39;.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), digits (<code>0-9</code>), <code>&#39; &#39;</code>, <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, and <code>&#39;.&#39;</code>.</li>
</ul>


<hr>

<h2>Approach: Sequential Parsing (Atoi Simulation)</h2>

<p>This problem asks us to implement behavior similar to the C/C++ <code>atoi()</code> function.</p>

<p>We scan the string from left to right and process characters in order.</p>

<p>Main steps:</p>

<ul>
    <li>Skip leading spaces</li>
    <li>Read optional sign (<code>+</code> or <code>-</code>)</li>
    <li>Read continuous digits</li>
    <li>Stop at first invalid character</li>
    <li>Clamp result to 32-bit signed integer range</li>
</ul>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def myAtoi(self, s: str) -&gt; int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i &lt; n and s[i] == ' ':
            i += 1

        if i &lt; n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i &lt; n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        result *= sign

        if result &lt; INT_MIN:
            return INT_MIN

        if result &gt; INT_MAX:
            return INT_MAX

        return result
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Initialize Variables</h3>

<pre>
i = 0
n = len(s)
sign = 1
result = 0
</pre>

<ul>
    <li><code>i</code> = current index</li>
    <li><code>n</code> = string length</li>
    <li><code>sign</code> = positive by default</li>
    <li><code>result</code> = stores final number</li>
</ul>

<hr>

<h3>Step 2: Define Integer Limits</h3>

<pre>
INT_MIN = -2147483648
INT_MAX = 2147483647
</pre>

<p>If result goes outside this range, it must be clamped.</p>

<hr>

<h3>Step 3: Skip Leading Spaces</h3>

<pre>
while i &lt; n and s[i] == ' ':
    i += 1
</pre>

<p>Example:</p>

<pre>
"   42"
</pre>

<p>After skipping spaces, pointer reaches:</p>

<pre>
'4'
</pre>

<hr>

<h3>Step 4: Read Optional Sign</h3>

<pre>
if i &lt; n and (s[i] == '+' or s[i] == '-'):
</pre>

<p>If sign is negative:</p>

<pre>
sign = -1
</pre>

<p>Examples:</p>

<pre>
"-42" → negative
"+42" → positive
</pre>

<hr>

<h3>Step 5: Read Digits</h3>

<pre>
while i &lt; n and s[i].isdigit():
</pre>

<p>Keep reading while characters are digits.</p>

<p>Build number:</p>

<pre>
result = result * 10 + digit
</pre>

<p>Example:</p>

<pre>
Input: "123"

0 * 10 + 1 = 1
1 * 10 + 2 = 12
12 * 10 + 3 = 123
</pre>

<hr>

<h3>Step 6: Stop at First Invalid Character</h3>

<p>Input:</p>

<pre>
"4193 with words"
</pre>

<p>Digits processed:</p>

<pre>
4193
</pre>

<p>Stops when reaching:</p>

<pre>
space
</pre>

<hr>

<h3>Step 7: Apply Sign</h3>

<pre>
result *= sign
</pre>

<p>Example:</p>

<pre>
42 with sign -1 = -42
</pre>

<hr>

<h3>Step 8: Clamp Overflow</h3>

<pre>
if result &lt; INT_MIN:
    return INT_MIN

if result &gt; INT_MAX:
    return INT_MAX
</pre>

<p>Examples:</p>

<pre>
"999999999999" → 2147483647
"-999999999999" → -2147483648
</pre>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
s = "   -42abc"
</pre>

<table>
<tr>
<th>Step</th>
<th>Action</th>
</tr>

<tr>
<td>1</td>
<td>Skip spaces</td>
</tr>

<tr>
<td>2</td>
<td>Read sign = -1</td>
</tr>

<tr>
<td>3</td>
<td>Read digits 4 and 2</td>
</tr>

<tr>
<td>4</td>
<td>Stop at 'a'</td>
</tr>

<tr>
<td>5</td>
<td>Apply sign</td>
</tr>
</table>

<p><strong>Output:</strong></p>

<pre>
-42
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<p>We scan the string once.</p>

<hr>

<h2>Why This Is Efficient</h2>

<ul>
    <li>Single pass through string</li>
    <li>No extra arrays or conversions needed</li>
    <li>Handles all edge cases cleanly</li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>This is a parsing problem, not a string-cleaning problem.</p>

<p>Read the string from left to right exactly once, follow the rules in order, and stop as soon as input becomes invalid.</p>
