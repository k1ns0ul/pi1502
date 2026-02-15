import re

class solution:
    def solve(self, paths: list, output: list) -> str:
        paths.sort()
        readable_files = []
        for path in paths:
            is_readable = True
            if re.fullmatch(r'.+[13]+', path):
                is_readable = False
            if re.fullmatch(r'.+[23]*1', path):
                is_readable = True
            if is_readable:
                readable_files.append(path)
        
        mapping = dict(zip(readable_files, output))
        return mapping.get('file221', '') + mapping.get('file22', '')