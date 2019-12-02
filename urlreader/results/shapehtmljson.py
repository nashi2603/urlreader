def shapehtmltojson(imgjsonlist):
    shapejsonlist = ''
    for i in imgjsonlist:
        shapejsonlist += '<div class="input-group my-1">'
        shapejsonlist += ('<input type="text" readonly class="form-control" value="' + i + '">')
        shapejsonlist += '<div class="input-group-append"><button type="button" class="btn bg-success">Button</button></div></div>'
    return shapejsonlist