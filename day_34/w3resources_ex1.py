# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

def format_string() -> str:
    out_str = ''
    out_str = '\n'
    out_str += 'Twinkle, twinkle, little star,' + '\n'
    out_str += '\t' + 'How I wonder what you are!' + '\n'
    out_str += '\t\t' + 'Up above the world so high,' + '\n'
    out_str += '\t\t' + 'Like a diamond in the sky.' + '\n'
    out_str += 'Twinkle, twinkle, little star,' + '\n'
    out_str += '\t' + 'How I wonder what you are'
    return out_str

sample_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

desired_output = """
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are"""

assert(format_string() == desired_output)

print(format_string())

print('passed')