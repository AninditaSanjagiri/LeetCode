<h2><a href="https://leetcode.com/problems/longest-palindromic-substring">Longest Palindromic Substring</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>


<hr>

<h2>Approach: Expand Around Center</h2>

<p>A palindrome reads the same forward and backward.</p>

<p>Instead of checking every possible substring, we treat each index as the <strong>center</strong> of a palindrome and expand outward while characters match.</p>

<p>Every palindrome has a center:</p>

<ul>
    <li><strong>Odd Length:</strong> <code>aba</code> → center is <code>b</code></li>
    <li><strong>Even Length:</strong> <code>abba</code> → center is between the two <code>b</code>'s</li>
</ul>

<p>So for every index, we check:</p>

<pre>
(i, i)     -> odd length palindrome
(i, i+1)   -> even length palindrome
</pre>

<p>This gives an efficient and clean solution.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):

            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) &gt; len(longest):
                longest = odd

            if len(even) &gt; len(longest):
                longest = even

        return longest
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Create Helper Function</h3>

<pre>
def expand(left, right):
</pre>

<p>This function expands outward from the center while characters match.</p>

<p>Example:</p>

<pre>
s = "racecar"
center = e
</pre>

<p>Expansion:</p>

<pre>
e
cec
aceca
racecar
</pre>

<hr>

<h3>Step 2: Expand While Valid</h3>

<pre>
while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:
</pre>

<p>Conditions:</p>

<ul>
    <li><code>left &gt;= 0</code> → stay inside left boundary</li>
    <li><code>right &lt; len(s)</code> → stay inside right boundary</li>
    <li><code>s[left] == s[right]</code> → still palindrome</li>
</ul>

<hr>

<h3>Step 3: Move Outward</h3>

<pre>
left -= 1
right += 1
</pre>

<p>Expand one step in both directions.</p>

<hr>

<h3>Step 4: Return Valid Palindrome</h3>

<pre>
return s[left + 1:right]
</pre>

<p>Why <code>left + 1</code>?</p>

<p>The loop stops after moving one step too far, so we return the last valid palindrome range.</p>

<hr>

<h3>Step 5: Check Every Index as Center</h3>

<pre>
for i in range(len(s)):
</pre>

<p>Each character can be the center of a palindrome.</p>

<hr>

<h3>Step 6: Odd Length Palindrome</h3>

<pre>
odd = expand(i, i)
</pre>

<p>Example:</p>

<pre>
"aba"
</pre>

<p>Center is the middle character.</p>

<hr>

<h3>Step 7: Even Length Palindrome</h3>

<pre>
even = expand(i, i + 1)
</pre>

<p>Example:</p>

<pre>
"abba"
</pre>

<p>Center lies between two characters.</p>

<hr>

<h3>Step 8: Store Longest Result</h3>

<pre>
if len(odd) &gt; len(longest):
    longest = odd

if len(even) &gt; len(longest):
    longest = even
</pre>

<p>Keep updating the best palindrome found so far.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
s = "babad"
</pre>

<h3>Index 0</h3>

<pre>
center = b
odd palindrome = "b"
</pre>

<h3>Index 1</h3>

<pre>
center = a
odd palindrome = "bab"
</pre>

<p>Longest becomes:</p>

<pre>
"bab"
</pre>

<h3>Index 2</h3>

<pre>
center = b
odd palindrome = "aba"
</pre>

<p>Same length as current answer.</p>

<p>Final answer can be:</p>

<pre>
"bab"
</pre>

<p>or</p>

<pre>
"aba"
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n²)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code></li>
</ul>

<hr>

<h2>Why This Is Efficient</h2>

<ul>
    <li>No need to check all substrings</li>
    <li>No extra DP table needed</li>
    <li>Uses only pointer expansion</li>
</ul>

<p>Much better than brute force <code>O(n³)</code>.</p>

<hr>

<h2>Key Insight</h2>

<p>Every palindrome grows from a center.</p>

<p>If we expand from every possible center, we are guaranteed to find the longest palindromic substring.</p>
