def shapehtmltojson(imgjsonlist, mode):
    shapejsonlist = ''
    j = 0
    for i in imgjsonlist:
        shapejsonlist += '<div class="input-group my-1">'
        shapejsonlist += ('<input id="' + str(j) + str(mode) + '" type="text" readonly class="form-control" value="' + i + '">')
        shapejsonlist += ('<div class="input-group-append"><button onclick="copybtn(\'' + str(j) + str(mode) + '\')" type="button" class="btn bg-success">Button</button></div></div>')
        j += 1
    return shapejsonlist
