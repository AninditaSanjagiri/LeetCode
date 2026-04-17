<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">Longest Substring Without Repeating Characters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3. Note that <code>&quot;bca&quot;</code> and <code>&quot;cab&quot;</code> are also correct answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

<hr>

<h2>Approach: Sliding Window + Hash Map</h2>

<p>To solve this problem efficiently, we use the <strong>Sliding Window</strong> technique along with a <strong>Hash Map (Dictionary)</strong>.</p>

<p>The idea is to maintain a window (substring) that always contains <strong>unique characters only</strong>.</p>

<ul>
    <li><code>left</code> → starting index of current window</li>
    <li><code>right</code> → ending index of current window</li>
    <li><code>seen</code> → stores the latest index of every character</li>
</ul>

<p>This allows us to process the string in linear time.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            if char in seen:
                left = max(left, seen[char] + 1)

            seen[char] = right
            longest = max(longest, right - left + 1)

        return longest
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Create Hash Map</h3>

<pre>
seen = {}
</pre>

<p>This dictionary stores:</p>

<pre>
character : latest index
</pre>

<p>Example:</p>

<pre>
{
 'a': 3,
 'b': 5
}
</pre>

<p>Meaning:</p>

<ul>
    <li><code>'a'</code> was last seen at index <code>3</code></li>
    <li><code>'b'</code> was last seen at index <code>5</code></li>
</ul>

<hr>

<h3>Step 2: Initialize Pointers</h3>

<pre>
left = 0
longest = 0
</pre>

<ul>
    <li><code>left</code> marks start of current valid substring</li>
    <li><code>longest</code> stores best answer so far</li>
</ul>

<hr>

<h3>Step 3: Traverse String</h3>

<pre>
for right in range(len(s)):
</pre>

<p>The <code>right</code> pointer moves through the string one character at a time.</p>

<hr>

<h3>Step 4: Current Character</h3>

<pre>
char = s[right]
</pre>

<p>Gets the current character being processed.</p>

<hr>

<h3>Step 5: If Duplicate Found</h3>

<pre>
if char in seen:
</pre>

<p>If the character was seen before, it may create a duplicate inside the current window.</p>

<p>So we move <code>left</code>:</p>

<pre>
left = max(left, seen[char] + 1)
</pre>

<p>This moves the left pointer just after the previous occurrence of that character.</p>

<h4>Why use max()?</h4>

<p>We never want <code>left</code> to move backward.</p>

<p>Example:</p>

<pre>
s = "abba"
</pre>

<p>When processing last <code>'a'</code>:</p>

<ul>
    <li>Old <code>'a'</code> index = <code>0</code></li>
    <li>Current <code>left</code> may already be <code>2</code></li>
</ul>

<pre>
left = max(2, 0 + 1) = 2
</pre>

<p>This keeps the window valid.</p>

<hr>

<h3>Step 6: Update Latest Position</h3>

<pre>
seen[char] = right
</pre>

<p>Store the most recent index of the current character.</p>

<p>Older indexes are no longer useful.</p>

<hr>

<h3>Step 7: Update Maximum Length</h3>

<pre>
longest = max(longest, right - left + 1)
</pre>

<p>Current window size is:</p>

<pre>
right - left + 1
</pre>

<p>If larger than previous answer, update <code>longest</code>.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
s = "abcabcbb"
</pre>

<table>
<tr>
<th>right</th>
<th>char</th>
<th>left</th>
<th>Current Window</th>
<th>longest</th>
</tr>
<tr>
<td>0</td>
<td>a</td>
<td>0</td>
<td>a</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>b</td>
<td>0</td>
<td>ab</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td>c</td>
<td>0</td>
<td>abc</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>a</td>
<td>1</td>
<td>bca</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>b</td>
<td>2</td>
<td>cab</td>
<td>3</td>
</tr>
</table>

<p>Final Answer = <code>3</code></p>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(min(n, charset))</code></li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>Instead of restarting every time a duplicate appears:</p>

<ul>
    <li>Expand window using <code>right</code></li>
    <li>Shrink window using <code>left</code></li>
    <li>Track latest indexes using hash map</li>
</ul>

<p>This gives an optimal linear-time solution.</p>
