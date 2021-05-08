import markdown

file = open('./markdown_example.md', 'r')

md_string = file.read()


""" Simple md to html """

html_string = markdown.markdown(md_string)  # Converts markdown to html

print(md_string)
print(html_string)
print()


""" md to html using Markdown() object """

md_obj = markdown.Markdown(extensions=['meta'])  # Initialize Markdown object

html_converted_string = md_obj.convert(md_string)  # Converts markdown to html
markdown_meta_data = md_obj.Meta  # Gets converted file meta data as dict

print(md_obj)
print(html_converted_string)
print(markdown_meta_data)
print()

md_obj.reset()  # Resets Markdown object

print(md_obj.Meta)  # This will return a empty dict
print()
