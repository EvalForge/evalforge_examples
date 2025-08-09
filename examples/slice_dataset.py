#!/usr/bin/env python3
import sys, json

def main():
    if len(sys.argv) != 3:
        print("Usage: slice_dataset.py <task> <input_jsonl>")
        sys.exit(2)
    task, path = sys.argv[1], sys.argv[2]
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if obj.get("task") == task:
                print(json.dumps(obj, ensure_ascii=False))

if __name__ == "__main__":
    main()
