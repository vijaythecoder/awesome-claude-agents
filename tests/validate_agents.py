#!/usr/bin/env python3
"""
Agent Validation Script
Validates Claude sub-agent files for correct format and quality standards.
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Try to import yaml, but provide fallback
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("Warning: PyYAML not installed. Using basic parser.")
    print("For full validation, install: pip install pyyaml")

class AgentValidator:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.valid_tools = [
            'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 
            'Grep', 'Glob', 'WebFetch', 'WebSearch', 
            'TodoWrite', 'ExitPlanMode', 'NotebookRead', 
            'NotebookEdit', 'LS', 'Task'
        ]
        
    def validate_agent_file(self, file_path: Path) -> Tuple[bool, List[str], List[str]]:
        """Validate a single agent file."""
        self.errors = []
        self.warnings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return False, self.errors, self.warnings
        
        # Check for YAML frontmatter
        if not content.startswith('---'):
            self.errors.append("File must start with YAML frontmatter (---)")
            return False, self.errors, self.warnings
        
        # Extract frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            self.errors.append("Invalid frontmatter format")
            return False, self.errors, self.warnings
        
        frontmatter = parts[1].strip()
        body = parts[2].strip()
        
        # Validate frontmatter
        self._validate_frontmatter(frontmatter)
        
        # Validate body content
        self._validate_body(body)
        
        # Check file naming
        self._validate_filename(file_path)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _parse_simple_yaml(self, yaml_str: str) -> Dict[str, str]:
        """Simple YAML parser for basic key-value pairs."""
        result = {}
        for line in yaml_str.strip().split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                result[key] = value
        return result
    
    def _validate_frontmatter(self, frontmatter: str):
        """Validate YAML frontmatter."""
        if HAS_YAML:
            try:
                data = yaml.safe_load(frontmatter)
            except yaml.YAMLError as e:
                self.errors.append(f"Invalid YAML in frontmatter: {e}")
                return
        else:
            # Use simple parser
            try:
                data = self._parse_simple_yaml(frontmatter)
            except Exception as e:
                self.errors.append(f"Failed to parse frontmatter: {e}")
                return
        
        if not isinstance(data, dict):
            self.errors.append("Frontmatter must be a YAML dictionary")
            return
        
        # Required fields
        if 'name' not in data:
            self.errors.append("Missing required field: name")
        else:
            # Validate name format
            name = data['name']
            if not re.match(r'^[a-z0-9-]+$', name):
                self.errors.append("Name must contain only lowercase letters, numbers, and hyphens")
            if len(name) < 3:
                self.errors.append("Name must be at least 3 characters long")
            if len(name) > 50:
                self.errors.append("Name must be less than 50 characters")
        
        if 'description' not in data:
            self.errors.append("Missing required field: description")
        else:
            desc = data['description']
            if len(desc) < 20:
                self.warnings.append("Description should be at least 20 characters for better auto-detection")
            if len(desc) > 500:
                self.warnings.append("Description is very long (>500 chars), consider making it more concise")
            if 'proactively' not in desc.lower() and 'use proactively' not in desc.lower():
                self.warnings.append("Consider adding 'use proactively' to description for automatic invocation")
        
        # Optional tools field
        if 'tools' in data:
            tools_str = data['tools']
            if not isinstance(tools_str, str):
                self.errors.append("Tools must be a comma-separated string")
            else:
                tools = [t.strip() for t in tools_str.split(',')]
                invalid_tools = [t for t in tools if t not in self.valid_tools]
                if invalid_tools:
                    self.errors.append(f"Invalid tools: {', '.join(invalid_tools)}")
                if len(tools) > 10:
                    self.warnings.append("Consider if all tools are necessary (>10 tools requested)")
    
    def _validate_body(self, body: str):
        """Validate agent body content."""
        if len(body) < 100:
            self.errors.append("Agent system prompt is too short (<100 characters)")
        
        if len(body) > 10000:
            self.warnings.append("Agent system prompt is very long (>10000 characters)")
        
        # Check for required sections
        required_sections = ['Core Expertise', 'Working Principles', 'Task Approach']
        for section in required_sections:
            if section not in body:
                self.warnings.append(f"Missing recommended section: {section}")
        
        # Check for code examples
        if '```' not in body:
            self.warnings.append("No code examples found - consider adding examples for clarity")
        
        # Check for proper markdown headers
        if not re.search(r'^#\s+', body, re.MULTILINE):
            self.warnings.append("No main header (# Title) found in body")
        
        # Check for list formatting
        if not re.search(r'^[-*]\s+', body, re.MULTILINE):
            self.warnings.append("No bullet lists found - consider using lists for better organization")
    
    def _validate_filename(self, file_path: Path):
        """Validate agent filename."""
        filename = file_path.stem
        if not re.match(r'^[a-z0-9-]+$', filename):
            self.errors.append("Filename should contain only lowercase letters, numbers, and hyphens")
        
        if not str(file_path).endswith('.md'):
            self.errors.append("Agent files must have .md extension")

def validate_directory(directory: Path) -> Tuple[int, int, int]:
    """Validate all agents in a directory."""
    validator = AgentValidator()
    total = 0
    passed = 0
    warnings_count = 0
    
    for agent_file in directory.rglob('*.md'):
        # Skip template and documentation files
        if 'template' in str(agent_file) or 'docs' in str(agent_file):
            continue
        
        total += 1
        print(f"\nValidating: {agent_file.relative_to(directory)}")
        
        is_valid, errors, warnings = validator.validate_agent_file(agent_file)
        
        if is_valid:
            passed += 1
            print("✅ PASSED")
        else:
            print("❌ FAILED")
            for error in errors:
                print(f"  ERROR: {error}")
        
        if warnings:
            warnings_count += len(warnings)
            for warning in warnings:
                print(f"  WARNING: {warning}")
    
    return total, passed, warnings_count

def main():
    """Main validation function."""
    if len(sys.argv) > 1:
        # Validate specific file
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        
        validator = AgentValidator()
        is_valid, errors, warnings = validator.validate_agent_file(file_path)
        
        if is_valid:
            print("✅ Agent validation PASSED")
        else:
            print("❌ Agent validation FAILED")
            for error in errors:
                print(f"  ERROR: {error}")
        
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"  WARNING: {warning}")
        
        sys.exit(0 if is_valid else 1)
    else:
        # Validate all agents
        agents_dir = Path(__file__).parent.parent / 'agents'
        if not agents_dir.exists():
            print(f"Error: Agents directory not found: {agents_dir}")
            sys.exit(1)
        
        print("Validating all agents...")
        print("=" * 50)
        
        total, passed, warnings_count = validate_directory(agents_dir)
        
        print("\n" + "=" * 50)
        print(f"Total agents: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Total warnings: {warnings_count}")
        
        if passed == total:
            print("\n✅ All agents passed validation!")
            sys.exit(0)
        else:
            print(f"\n❌ {total - passed} agents failed validation")
            sys.exit(1)

if __name__ == "__main__":
    main()