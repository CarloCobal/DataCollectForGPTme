import json

def tokenize(content):
    # Simplified tokenization by splitting based on spaces
    return content.split()

def chunk_messages_with_labels(messages, token_limit=127990):
    chunks = {}
    current_chunk = []
    current_chunk_label = 1
    current_tokens = 0
    
    for message in messages:
        formatted_message = f"{message['author_role']}: {message['content']}"
        message_tokens = len(tokenize(formatted_message))
        
        if current_tokens + message_tokens > token_limit:
            # Finalize the current chunk and start a new one
            chunks[f"chunk_{current_chunk_label}"] = current_chunk
            current_chunk_label += 1
            current_chunk = [message]
            current_tokens = message_tokens
        else:
            current_chunk.append(message)
            current_tokens += message_tokens
    
    # Add the last chunk if it has any messages
    if current_chunk:
        chunks[f"chunk_{current_chunk_label}"] = current_chunk
    
    return chunks

# Load the flattened messages from JSON
json_file_path = 'flattened_messages.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    messages = json.load(file)

# Create chunks with labels, each containing a list of messages
token_limit = 127990  # Adjust this token limit as needed
labeled_chunks = chunk_messages_with_labels(messages, token_limit)

# Save the labeled chunks to a new JSON file
new_json_file_path = 'labeled_message_chunks.json'
with open(new_json_file_path, 'w', encoding='utf-8') as new_file:
    json.dump(labeled_chunks, new_file, ensure_ascii=False, indent=4)

print(f"Labeled chunked messages saved to {new_json_file_path}")
