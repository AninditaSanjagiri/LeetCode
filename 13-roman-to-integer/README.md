<h2><a href="https://leetcode.com/problems/roman-to-integer">Roman to Integer</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two ones added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;III&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;LVIII&quot;
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;MCMXCIV&quot;
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s</code> contains only&nbsp;the characters <code>(&#39;I&#39;, &#39;V&#39;, &#39;X&#39;, &#39;L&#39;, &#39;C&#39;, &#39;D&#39;, &#39;M&#39;)</code>.</li>
	<li>It is <strong>guaranteed</strong>&nbsp;that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>



<hr>

<h2>Approach: Compare Current Symbol with Next Symbol</h2>

<p>Roman numerals are usually formed by adding values from left to right.</p>

<p>Example:</p>

<pre>
VIII = 5 + 1 + 1 + 1 = 8
LX = 50 + 10 = 60
</pre>

<p>However, when a smaller numeral appears before a larger numeral, it means subtraction.</p>

<p>Examples:</p>

<pre>
IV = 5 - 1 = 4
IX = 10 - 1 = 9
XL = 50 - 10 = 40
CM = 1000 - 100 = 900
</pre>

<p>So while traversing the string:</p>

<ul>
    <li>If current value &lt; next value → subtract current</li>
    <li>Otherwise → add current</li>
</ul>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def romanToInt(self, s: str) -&gt; int:

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i &lt; len(s) - 1 and values[s[i]] &lt; values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Store Roman Values</h3>

<pre>
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
</pre>

<p>This dictionary allows instant lookup of each Roman numeral value.</p>

<hr>

<h3>Step 2: Initialize Result</h3>

<pre>
total = 0
</pre>

<p>This stores the final integer value.</p>

<hr>

<h3>Step 3: Traverse the String</h3>

<pre>
for i in range(len(s)):
</pre>

<p>Process one Roman symbol at a time.</p>

<hr>

<h3>Step 4: Check Next Character</h3>

<pre>
if i &lt; len(s) - 1 and values[s[i]] &lt; values[s[i + 1]]:
</pre>

<p>We first ensure a next character exists.</p>

<p>Then compare current symbol with next symbol.</p>

<hr>

<h3>Step 5: Subtract if Smaller Before Larger</h3>

<pre>
total -= values[s[i]]
</pre>

<p>Examples:</p>

<pre>
IV:
I &lt; V → subtract 1

IX:
I &lt; X → subtract 1
</pre>

<hr>

<h3>Step 6: Otherwise Add Normally</h3>

<pre>
total += values[s[i]]
</pre>

<p>Examples:</p>

<pre>
VI:
V &gt; I → add 5
I last symbol → add 1
</pre>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
s = "MCMIV"
</pre>

<table>
<tr>
<th>Index</th>
<th>Symbol</th>
<th>Next</th>
<th>Action</th>
<th>Total</th>
</tr>

<tr>
<td>0</td>
<td>M</td>
<td>C</td>
<td>Add 1000</td>
<td>1000</td>
</tr>

<tr>
<td>1</td>
<td>C</td>
<td>M</td>
<td>Subtract 100</td>
<td>900</td>
</tr>

<tr>
<td>2</td>
<td>M</td>
<td>I</td>
<td>Add 1000</td>
<td>1900</td>
</tr>

<tr>
<td>3</td>
<td>I</td>
<td>V</td>
<td>Subtract 1</td>
<td>1899</td>
</tr>

<tr>
<td>4</td>
<td>V</td>
<td>-</td>
<td>Add 5</td>
<td>1904</td>
</tr>
</table>

<p><strong>Output:</strong></p>

<pre>
1904
</pre>

<hr>

<h2>More Examples</h2>

<pre>
III   = 3
LVIII = 58
MCMXCIV = 1994
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<p>Where <code>n</code> is length of the Roman numeral string.</p>

<hr>

<h2>Why This Is Efficient</h2>

<ul>
    <li>Single pass through the string</li>
    <li>Constant-time dictionary lookups</li>
    <li>No special-case hardcoding required</li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>Roman numerals become simple once you notice this rule:</p>

<pre>
Smaller before larger = subtract
Otherwise = add
</pre>

<p>Apply that rule while scanning left to right.</p>
