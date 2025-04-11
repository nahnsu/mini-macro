import json
import re
from typing import Dict, Any, Optional


def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    json_matches = re.findall(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    for match in json_matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue

    brace_match = re.search(r"(\{.*\})", text, re.DOTALL)
    if brace_match:
        try:
            return json.loads(brace_match.group(1))
        except json.JSONDecodeError:
            pass

    return None
