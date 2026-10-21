#!/usr/bin/env python3
"""
Validate SKILL.md frontmatter是否符合规范
"""
import re
import sys
from pathlib import Path

def validate_frontmatter(skill_path: str) -> bool:
    """验证 SKILL.md 的 frontmatter"""
    path = Path(skill_path)
    if not path.exists():
        print(f"❌ File not found: {skill_path}")
        return False
    
    content = path.read_text(encoding='utf-8')
    
    # 检查 frontmatter 格式
    if not content.startswith('---'):
        print("❌ Missing frontmatter start '---'")
        return False
    
    second_dash = content.find('---', 3)
    if second_dash == -1:
        print("❌ Missing frontmatter end '---'")
        return False
    
    frontmatter = content[3:second_dash].strip()
    
    # 检查必需字段
    required_fields = ['name', 'description']
    for field in required_fields:
        if not re.search(rf'^{field}:', frontmatter, re.MULTILINE):
            print(f"❌ Missing required field: {field}")
            return False
    
    # 检查 description 是否包含触发器
    desc_match = re.search(r'description:\s*(.+)', frontmatter, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1)
        if 'Use when' not in desc and 'NOT for' not in desc:
            print("⚠️  Warning: description should include 'Use when' and 'NOT for'")
    
    print(f"✅ Frontmatter validated for {path.name}")
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        skill_file = sys.argv[1]
    else:
        skill_file = 'SKILL.md'
    
    success = validate_frontmatter(skill_file)
    sys.exit(0 if success else 1)
