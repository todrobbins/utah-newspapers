import json

with open('utah-newspapers.json', 'r') as f:
    data = json.loads(f.read())

with open('output.html', 'w') as f:
    f.write('<table>\n')
    f.write('<tbody>\n')

    # Hardcoding this since it's easier
    f.write('<tr>\n')
    f.write('\t<th class="title-cell">Title</th>\n')
    f.write('\t<th class="city-cell">City</th>\n')
    f.write('\t<th class="county-cell">County</th>\n')
    f.write('\t<th class="from-cell">From</th>\n')
    f.write('\t<th class="to-cell">To</th>\n')
    f.write('</tr>\n')

    for title in data:
        newspaper = data[title]
        f.write('<tr>\n')
        f.write('\t<th class="title-cell">{}</th>\n'.format(title.strip()))
        f.write('\t<td class="city-cell">{}</td>\n'.format(newspaper['city'].strip()))
        f.write('\t<td class="county-cell">{}</td>\n'.format(newspaper['county'].strip()))
        f.write('\t<td class="from-cell">{}</td>\n'.format(newspaper['from'].strip()))
        f.write('\t<td class="to-cell">{}</td>\n'.format(newspaper['to'].strip()))
        f.write('</tr>\n')
    f.write('</tbody>\n')
    f.write('</table>')