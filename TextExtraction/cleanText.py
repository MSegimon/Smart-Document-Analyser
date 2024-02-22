import json

def filter_content(content, min_paragraph_length=80):
    # Step 1: Filter out short paragraphs
    intermediate_content = [(tag, text) for tag, text in content if not (tag == 'p' and len(text) < min_paragraph_length)]
    
    # Step 2: Remove trailing headings
    # Find the last paragraph to determine where to stop removing headings
    last_paragraph_index = None
    for i in range(len(intermediate_content) - 1, -1, -1):
        if intermediate_content[i][0] == 'p':
            last_paragraph_index = i
            break
    
    # If there's no paragraph at all, return an empty list to indicate no valid content
    if last_paragraph_index is None:
        return []
    
    # Remove trailing headings by slicing the list up to and including the last paragraph
    filtered_content = intermediate_content[:last_paragraph_index + 1]
    
    return filtered_content

def generate_json_from_content(content):
    root = []  # Root list to hold the entire document structure
    stack = [root]  # Stack to keep track of current nesting level

    for tag, text in content:
        item = {"tag": tag, "text": text, "content": []}

        # Determine the current level based on tag
        if tag.startswith('h'):
            level = int(tag[1])
        else:
            level = float('inf')  # Treat non-headings as the deepest level

        # Pop from stack until we find the parent level
        while len(stack) > level:
            stack.pop()

        # Append the current item to the appropriate level
        if tag.startswith('h'):
            stack[-1].append(item)  # Append to the current level
            stack.append(item["content"])  # Push the new level onto the stack for headings
        else:
            stack[-1].append(item)  # Append paragraphs directly to the current heading content

    return root
