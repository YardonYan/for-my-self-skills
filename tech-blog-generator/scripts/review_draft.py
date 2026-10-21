#!/usr/bin/env python3
"""
Self-review helper: scans an output file against style rules.
Checks for forbidden phrases, filler words, and passive voice patterns.
"""
import re
import sys
from pathlib import Path
from collections import Counter

# Forbidden patterns with suggested replacements
FORBIDDEN_PATTERNS = [
    (r'let\'s learn', 'pedagogical tone — remove'),
    (r'I hope this helps', 'service-desk tone — remove'),
    (r'in today\'s digital landscape', 'AI fluff — remove'),
    (r'in today\'s fast-paced world', 'AI fluff — remove'),
    (r'unlock the power of', 'dying metaphor — rewrite'),
    (r'game-changer', 'dying metaphor — rewrite'),
    (r'cutting-edge', 'dying metaphor — rewrite'),
    (r'Keep coding!', 'emotional sign-off — remove'),
    (r'Happy learning!', 'emotional sign-off — remove'),
    (r'Stay tuned!', 'ceremonial closing — remove'),
    (r'it is important to note that', 'filler phrase — delete and state fact'),
    (r'it is worth mentioning that', 'filler phrase — delete and state fact'),
    (r'in order to', 'filler — replace with "to"'),
    (r'due to the fact that', 'filler — replace with "because"'),
    (r'at this point in time', 'filler — replace with "now"'),
    (r'may potentially', 'redundant hedge — use "may"'),
    (r'could possibly', 'redundant hedge — use "could"'),
    (r'utilize', 'jargon — replace with "use"'),
    (r'leverage', 'jargon — replace with "use" or explain'),
    (r'significantly', 'vague — quantify'),
    (r'significant', 'vague — quantify'),
    (r'robust', 'vague — explain mechanism'),
    (r'optimized', 'vague — give before/after numbers'),
    (r'powerful', 'vague — list specific capability'),
    (r'Furthermore,', 'transition overuse — consider removing'),
    (r'Moreover,', 'transition overuse — consider removing'),
    (r'Additionally,', 'transition overuse — consider removing'),
]

# Passive voice heuristic patterns
PASSIVE_PATTERNS = [
    r'\b(was|were|is|are|been|being)\s+(\w+ed|built|made|done|taken|given|seen|found|shown|written|run|set)\b',
    r'\b(can be|could be|should be|will be|has been|have been)\s+\w+ed\b',
]


def count_issues(filepath: str) -> dict:
    """Scan file for style violations."""
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        return {}
    
    content = path.read_text(encoding='utf-8')
    issues = {}
    
    # Check forbidden patterns
    for pattern, description in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            issues[description] = len(matches)
    
    # Check passive voice
    passive_count = 0
    for pattern in PASSIVE_PATTERNS:
        passive_count += len(re.findall(pattern, content, re.IGNORECASE))
    if passive_count > 5:
        issues[f"passive constructions (>{passive_count})"] = passive_count
    
    # Check vague descriptors in context
    vague_terms = ['efficient', 'robust', 'optimized', 'powerful', 'scalable']
    for term in vague_terms:
        # Find term not followed by a number within 20 chars
        pattern = rf'\b{term}\b(?![\s\S]{{0,20}}\d)'
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            issues[f'"{term}" without quantification'] = len(matches)
    
    # Check consecutive sentence starters
    sentences = re.findall(r'[.!?]\s+(\w+)', content)
    if sentences:
        starter_counts = Counter(s.lower() for s in sentences)
        for word, count in starter_counts.most_common(5):
            if count >= 4:
                issues[f'repeated sentence starter "{word}" ({count}x)'] = count
    
    # Count code blocks and check for explanations
    code_blocks = len(re.findall(r'```\w*\n', content))
    file_refs = len(re.findall(r'[.\w]+\.\w+:\d+', content))
    if code_blocks > 0 and file_refs == 0:
        issues["code blocks without file references"] = code_blocks
    elif file_refs < code_blocks:
        issues[f"some code blocks lack file references ({code_blocks} blocks, {file_refs} refs)"] = code_blocks - file_refs
    
    return issues


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Usage: python review_draft.py <output-file.md>")
        sys.exit(1)
    
    issues = count_issues(filepath)
    
    if not issues:
        print(f"✅ {filepath}: No style issues detected")
        return
    
    print(f"📊 Review: {filepath}")
    print(f"{'='*60}")
    
    total = 0
    for issue, count in sorted(issues.items(), key=lambda x: -x[1]):
        print(f"  ⚠️  {issue} ({count} occurrence{'s' if count > 1 else ''})")
        total += count
    
    print(f"{'='*60}")
    print(f"📊 Total issues: {total}")
    
    if total > 10:
        print("🔴 High issue count — consider rewriting sections")
    elif total > 5:
        print("🟡 Moderate issue count — review flagged items")
    else:
        print("🟢 Low issue count — fix remaining items before publishing")


if __name__ == '__main__':
    main()
