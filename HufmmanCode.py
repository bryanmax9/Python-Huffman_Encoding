# Import necessary libraries
import heapq  # Used to create a priority queue
from collections import defaultdict  # Used to store character frequencies

# Define a class to represent nodes in the Huffman tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # Character stored in the node
        self.freq = freq  # Frequency of the character in the input
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

    def __lt__(self, other):
        return self.freq < other.freq  # Comparison method for sorting

# Function to build the Huffman tree
def build_huffman_tree(string):
    # Calculate character frequencies and store them in a dictionary
    char_freq = defaultdict(int)
    for char in string:
        char_freq[char] += 1

    # Create a priority queue (min heap) for Huffman nodes
    min_heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(min_heap)  # Convert the list into a heap

    # Build the Huffman tree by repeatedly merging nodes
    while len(min_heap) > 1:
        left_node = heapq.heappop(min_heap)  # Pop the node with the lowest frequency
        right_node = heapq.heappop(min_heap)
        # Create a new node with no character and a frequency equal to the sum of children's frequencies
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node  # Set left child
        merged_node.right = right_node  # Set right child
        heapq.heappush(min_heap, merged_node)  # Push the merged node back to the heap

    return min_heap[0]  # Return the root of the Huffman tree

# Function to calculate the length of Huffman encoding
def calculate_huffman_encoding_length(node, length=0):
    if node is None:
        return 0
    if node.char is not None:
        return node.freq * length
    return (calculate_huffman_encoding_length(node.left, length + 1) +
            calculate_huffman_encoding_length(node.right, length + 1))

# Function to calculate Huffman encoding length for a given input string
def huffman_encoding_length(input_string):
    root = build_huffman_tree(input_string)
    return calculate_huffman_encoding_length(root)

# Main function
def main():
    # Read input from a file
    file_path = "10.txt"  # Replace with the path to your input file
    with open(file_path, "r") as file:
        input_string = file.read().strip()

    # Calculate Huffman encoding length for the input string
    length = huffman_encoding_length(input_string)

    # Print the result
    print(f"The length of Huffman encoding for the input from '{file_path}' is {length} bits.")

# Entry point of the script
if __name__ == "__main__":
    main()
