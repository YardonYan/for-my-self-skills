#!/usr/bin/env python3
"""
检查输出是否超过 token 限制 (约 5k tokens = ~20KB)
"""
import sys
from pathlib import Path

# 估算: 1 token ≈ 4 字符 (英文) 或 1.5 字符 (中文)
# 安全阈值: 5000 tokens ≈ 20000 字符

DEFAULT_LIMIT = 20000

def count_tokens(text: str) -> int:
    """估算 token 数量"""
    chinese = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    english = len([c for c in text if c.isascii()])
    # 中文 1.5 字符 ≈ 1 token, 英文 4 字符 ≈ 1 token
    return int(chinese / 1.5 + english / 4)

def check_length(file_path: str, limit: int = DEFAULT_LIMIT) -> bool:
    """检查文件长度"""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return False
    
    content = path.read_text(encoding='utf-8')
    tokens = count_tokens(content)
    
    print(f"📊 {path.name}: ~{tokens} tokens ({len(content)} chars)")
    
    if tokens > limit:
        print(f"⚠️  Warning: Exceeds {limit} tokens (~{tokens - limit} over)")
        return False
    
    print(f"✅ Within limit ({limit} tokens)")
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = 'SKILL.md'
    
    limit = DEFAULT_LIMIT
    if len(sys.argv) > 2:
        limit = int(sys.argv[2])
    
    success = check_length(file_path, limit)
    sys.exit(0 if success else 1)
