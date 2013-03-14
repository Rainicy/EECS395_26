def commonTokensListToSVGImage(tokens, width=740, height=500):
    svg_string = """<svg version="1.1" baseProfile="tiny" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width=\"""" + str(width) + """px" height=\"""" + str(height) + """px" ><rect x="0px" y="0px" width=\"""" + str(width) + """px" height=\"""" + str(height) + """px" fill="lime" />"""

    tokens = normalizeToHeight(tokens, height)
    y = 0
    for s,t in tokens:
        y += t
        svg_string += '<text x="0px" y="' + str(y) + '" font-size="' + str(t) + '">'
        svg_string += s + "</text>"
    svg_string += '</svg>'
    svg_string = svg_string.strip()
    svg_string = svg_string.replace("\n", " ")
    svg_string = unicode(svg_string)
    return svg_string

def normalizeToHeight(tokens, height):
    normalized = []
    total = sum(map(lambda b: b[1], tokens))
    for s,n in tokens:
        normalized.append(tuple([s, height * n / total]))
    return normalized
