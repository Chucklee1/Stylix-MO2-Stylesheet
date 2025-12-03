import json, re, os

tool_root = './'
palette_path  = f'{tool_root}/palette.json'
template_path = f'{tool_root}/Stylix.qss.mustache'
target_path   = '/path/to/your/modorganizer2/stylesheets/Stylix.qss'

# read json, store in dictionary,
with open(palette_path, 'r') as file:
    palette = json.load(file)

print(f"current palette: {palette}") # debug

# append '#' to all values
# for key in palette:
#    palette[key] = "#" + palette[key]

# read template, replace all {{basexx}}
# with hex color values
with open(template_path, 'r') as file:
    content = file.read()

pattern = r'\{\{(\w+)\}\}'

def replacer(match):
    key = match.group(1)
    return palette.get(key, match.group(0))  # replace or leave as is

target_contents = re.sub(pattern, replacer, content)

# write to target
with open(target_path, 'w') as file:
    file.write(target_contents)

print(f"Wrote contents to: {target_path}") # debug
