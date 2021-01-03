import re
'#(.a$@&'
re.search('\w', '#(.a$@&')
#so \w is essentially shorthand for [a-zA-Z0-9_]
re.search('[a-zA-Z0-9_]', '#(.a$@&')
<re.Match object; span=(3, 4), match='a'>
#\W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
re.search('\W', 'a_1*3Qb')
re.search('[^a-zA-Z0-9_]','#(.a$@&' )
#\W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
re.search('\W', 'a_1*3Qb')
re.search('[^a-zA-Z0-9_]','#(.a$@&' )
<re.Match object; span=(0, 1), match='#'>
#
#\d matches any decimal digit character. \D is the opposite. It matches any character that isn’t a decimal digit:
re.search('\d', 'abc4def')
re.search('\D', '234Q678')
re.search('\s', 'foo barbaz')
re.search('\S', '  \n foo  \n  ')
#\S is the opposite of \s. It matches any character that isn’t whitespace:
#\d is essentially equivalent to [0-9], and \D is equivalent to [^0-9]
<re.Match object; span=(3, 4), match='Q'>
re.search('^foo', 'foobar')
re.search('\Afoo', 'foobar')
re.search('bar$', 'foobar')
re.search('bar\Z', 'foobar')
<re.Match object; span=(3, 6), match='bar'>
#\b asserts that the regex parser’s current position must be at the beginning or end of a word.
re.search(r'\bbar', 'foo bar')
re.search(r'foo\b', 'foo bar')
<re.Match object; span=(0, 3), match='foo'>
​
