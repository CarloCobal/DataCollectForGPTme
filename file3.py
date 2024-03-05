import json

def save_chunk_to_file(json_file_path, output_file_path="current_chunk.txt"):
    # Load the chunked messages from the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        chunks = json.load(file)
    
    # Ask the user for the chunk label they want to save
    chunk_label = input("Enter the chunk label (e.g., 'chunk_1'): ").strip()
    
    # Save the content of the specified chunk to a file if it exists
    if chunk_label in chunks:
        # Convert the list of messages to a single string
        chunk_content = '\n'.join([f"{msg['author_role']}: {msg['content']}" for msg in chunks[chunk_label]])
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(chunk_content)
        print(f"Content of {chunk_label} has been saved to {output_file_path}.")
    else:
        print("Error: The specified chunk label does not exist in the file.")

# Specify the path to your labeled_message_chunks.json file
json_file_path = 'labeled_message_chunks.json'

# Call the function to save the specified chunk to a file
save_chunk_to_file(json_file_path)
