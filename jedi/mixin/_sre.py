def compile():
    class SRE_Match():
        endpos = 1
        lastgroup = 0
        lastindex = 1
        pos = 0
        string = 'a'
        regs = ((0, 1),)

        def __init__(self, pattern):
            self.re = pattern

        def start(self):
            return 0

        def end(self):
            return 1

        def span(self):
            return 0, 1

        def expand(self):
            return ''

        def group(self):
            return ''

        def groupdict(self):
            return {'a', 'a'}

        def groups(self):
            return ('a',)

    class SRE_Pattern():
        flags = 0
        groupindex = {}
        groups = 0
        pattern = 'a'

        def findall(self):
            """
            findall(string[, pos[, endpos]]) --> list.
            Return a list of all non-overlapping matches of pattern in string.
            """
            return ['a']

        def finditer(self):
            """
            finditer(string[, pos[, endpos]]) --> iterator.
            Return an iterator over all non-overlapping matches for the
            RE pattern in string. For each match, the iterator returns a
            match object.
            """
            yield SRE_Match(self)

        def match(self):
            """
            match(string[, pos[, endpos]]) --> match object or None.
            Matches zero or more characters at the beginning of the string
            pattern
            """
            return SRE_Match(self)

        def scanner(self):
            pass

        def search(self):
            """
            search(string[, pos[, endpos]]) --> match object or None.
            Scan through string looking for a match, and return a corresponding
            MatchObject instance. Return None if no position in the string matches.
            """
            return SRE_Match(self)

        def split(self):
            """
            split(string[, maxsplit = 0])  --> list.
            Split string by the occurrences of pattern.
            """
            return ['a']

        def sub(self):
            """
            sub(repl, string[, count = 0]) --> newstring
            Return the string obtained by replacing the leftmost non-overlapping
            occurrences of pattern in string by the replacement repl.
            """
            return ''

        def subn(self):
            """
            subn(repl, string[, count = 0]) --> (newstring, number of subs)
            Return the tuple (new_string, number_of_subs_made) found by replacing
            the leftmost non-overlapping occurrences of pattern with the
            replacement repl.
            """
            return ('', 1)

    return SRE_Pattern()
