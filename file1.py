import json
import os

def tokenize(content):
    return content.split()

def save_chunks_to_files(messages, folder_path, token_limit=127990):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    current_chunk = []
    current_chunk_label = 1
    current_tokens = 0
    
    for message in messages:
        formatted_message = f"{message['author_role']}: {message['content']}"
        message_tokens = len(tokenize(formatted_message))
        
        if current_tokens + message_tokens > token_limit:
            # Save the current chunk to a file
            chunk_file_path = os.path.join(folder_path, f"chunk_{current_chunk_label}.txt")
            with open(chunk_file_path, 'w', encoding='utf-8') as chunk_file:
                chunk_content = "\n".join([f"{msg['author_role']}: {msg['content']}" for msg in current_chunk])
                chunk_file.write(chunk_content)
            
            # Start a new chunk
            current_chunk_label += 1
            current_chunk = [message]
            current_tokens = message_tokens
        else:
            current_chunk.append(message)
            current_tokens += message_tokens
    
    # Save the last chunk if it has any messages
    if current_chunk:
        chunk_file_path = os.path.join(folder_path, f"chunk_{current_chunk_label}.txt")
        with open(chunk_file_path, 'w', encoding='utf-8') as chunk_file:
            chunk_content = "\n".join([f"{msg['author_role']}: {msg['content']}" for msg in current_chunk])
            chunk_file.write(chunk_content)

# Load the flattened messages from JSON
json_file_path = 'flattened_messages.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    messages = json.load(file)

# Define the folder path where the chunks will be saved
folder_path = 'chunks_folder'

# Call the function to create chunks and save them to separate files
save_chunks_to_files(messages, folder_path, token_limit=127990)

print(f"Chunks saved to separate files in {folder_path}")
