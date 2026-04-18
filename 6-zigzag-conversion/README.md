<h2><a href="https://leetcode.com/problems/zigzag-conversion">Zigzag Conversion</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 4
<strong>Output:</strong> &quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A&quot;, numRows = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>&#39;,&#39;</code> and <code>&#39;.&#39;</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>



<hr>

<h2>Approach: Row Simulation (Zigzag Traversal)</h2>

<p>Instead of building a full 2D zigzag grid, we simulate the movement row by row.</p>

<p>We create one string for each row and place characters while moving:</p>

<ul>
    <li>Downward from top row to bottom row</li>
    <li>Then upward diagonally back to top row</li>
</ul>

<p>This repeating movement forms the zigzag pattern.</p>

<hr>

<h2>Python Code</h2>

<pre>
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows &gt;= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        goingDown = False

        for char in s:
            rows[currentRow] += char

            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currentRow += 1
            else:
                currentRow -= 1

        return "".join(rows)
</pre>

<hr>

<h2>Detailed Explanation</h2>

<h3>Step 1: Handle Edge Cases</h3>

<pre>
if numRows == 1 or numRows &gt;= len(s):
    return s
</pre>

<p>If only one row exists, or rows are more than string length, no zigzag transformation happens.</p>

<p>Example:</p>

<pre>
s = "ab"
numRows = 4
</pre>

<p>Output remains:</p>

<pre>
ab
</pre>

<hr>

<h3>Step 2: Create Storage for Rows</h3>

<pre>
rows = [""] * numRows
</pre>

<p>If <code>numRows = 4</code>:</p>

<pre>
["", "", "", ""]
</pre>

<p>Each index represents one zigzag row.</p>

<hr>

<h3>Step 3: Initialize Position Variables</h3>

<pre>
currentRow = 0
goingDown = False
</pre>

<ul>
    <li><code>currentRow</code> = row currently receiving characters</li>
    <li><code>goingDown</code> = direction of movement</li>
</ul>

<p>Meaning:</p>

<ul>
    <li><code>True</code> → move downward</li>
    <li><code>False</code> → move upward</li>
</ul>

<hr>

<h3>Step 4: Traverse Each Character</h3>

<pre>
for char in s:
</pre>

<p>Process characters one by one.</p>

<hr>

<h3>Step 5: Add Character to Current Row</h3>

<pre>
rows[currentRow] += char
</pre>

<p>Example:</p>

<pre>
rows = ["PA", "AP", "Y"]
currentRow = 1
char = "L"
</pre>

<p>After update:</p>

<pre>
rows = ["PA", "APL", "Y"]
</pre>

<hr>

<h3>Step 6: Reverse Direction at Top or Bottom</h3>

<pre>
if currentRow == 0 or currentRow == numRows - 1:
    goingDown = not goingDown
</pre>

<p>Whenever we reach:</p>

<ul>
    <li>Top row</li>
    <li>Bottom row</li>
</ul>

<p>We reverse movement direction.</p>

<hr>

<h3>Step 7: Move to Next Row</h3>

<pre>
if goingDown:
    currentRow += 1
else:
    currentRow -= 1
</pre>

<p>This creates the zigzag row order.</p>

<hr>

<h2>Row Movement Example</h2>

<p><strong>numRows = 4</strong></p>

<pre>
0 → 1 → 2 → 3 → 2 → 1 → 0 → 1 → 2 → 3 ...
</pre>

<p>Rows go downward, then upward, repeatedly.</p>

<hr>

<h2>Dry Run</h2>

<p><strong>Input:</strong></p>

<pre>
s = "PAYPALISHIRING"
numRows = 3
</pre>

<p>Zigzag Pattern:</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>Row strings become:</p>

<pre>
row0 = "PAHN"
row1 = "APLSIIG"
row2 = "YIR"
</pre>

<p>Final Output:</p>

<pre>
PAHNAPLSIIGYIR
</pre>

<hr>

<h2>Complexity Analysis</h2>

<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code></li>
    <li><strong>Space Complexity:</strong> <code>O(n)</code></li>
</ul>

<p>Where <code>n</code> is length of string.</p>

<hr>

<h2>Why This Is Efficient</h2>

<ul>
    <li>No 2D matrix needed</li>
    <li>Each character processed once</li>
    <li>Direct row-building approach</li>
</ul>

<hr>

<h2>Key Insight</h2>

<p>The zigzag pattern is just repeated row movement:</p>

<pre>
down → up → down → up
</pre>

<p>Track the current row and direction, place characters accordingly, then join all rows.</p>
