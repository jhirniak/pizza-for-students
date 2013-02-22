
var TABLE_BG_OPACITY = 0.15,
    TABLE_TRANSITION_OPACITY = 1,
    TABLE_OPACITY = 1;
    

var tableW = 0,
    tableH = 280,
    tableX,
    tableY;

//var tableShown;

var tablePanel;

var transitionPanel;

function setupTable() {
    tablePanel = svg.append('g')
        .attr('class', 'tableGroup');

    transitionPanel = svg.append('g')
        .attr('class', 'transitionPanel');

    transitionPanel.append('path')
        .attr('class', 'transitionBg')
}

var lineFunction = d3.svg.line()
                         .x(function (d, i) { return d.x; })
                         .y(function (d, i) { return d.y; })

function showTable(data, startX, startY, startW, tX, tY, tw) {


    //args to vars
    tableW = tw;
    tableX = tX;
    tableY = tY;

    //draw background (shade)
    var off = (CONTENT_OFFSET * dayLength);
    var pts = [{ x: dayLength * sliderPos, y: barHeight },
             { x: tableX - off, y: tableY },
             { x: tableX - off, y: tableY + tableH + off },
             { x: tableX + tableW + off, y: tableY + tableH + off },
             { x: tableX + tableW + off, y: tableY },
             { x: dayLength * (sliderPos + 1), y: barHeight }];

    tablePanel.select('path.transitionBg')
            .attr("d", lineFunction(pts))

    //transition
    var tr = transitionPanel.selectAll('path.transition')
                .data(data);
    tr.enter()
        .append('path')
        .attr('class', 'transition')
        .attr('fill', function (d, i) { return sliderGetColor(i); })
    tr.exit()
        .remove();
    tr
        .transition().duration(TRANSITION_TIME)
        .attr('d', function (d, i) {
            var pts = [{ x: startX + d.position * startW / contentLen, y: startY },
                        { x: startX + d.position * startW / contentLen, y: startY + barHeight / 10 },
                        { x: tableX + d.position * tableW / contentLen, y: tableY },
                        { x: tableX + (d.position + d.size) * tableW / contentLen, y: tableY },
                        { x: startX + (d.position + d.size) * startW / contentLen, y: startY + barHeight / 10 },
                        { x: startX + (d.position + d.size) * startW / contentLen, y: startY }];
            return lineFunction(pts);
        })
        .attr('fill', function (d, i) { return sliderGetColor(i); })

    var pans = tablePanel.selectAll('rect.panel')
        .data(data);
    pans.enter()
        .append('rect')
        .attr('class', 'panel')
        .attr('height', tableH)
        .attr('y', tableY - 0.5)
        .attr('x', function (d, i) {
            return (i == 0) ? 0 : tableW;
        });
        
    pans.exit()
        .remove();
    pans
        .transition().duration(TRANSITION_TIME)
        .attr('x', function(d, i) {
            return tableX + d.position * tableW / contentLen;
        })
        .attr('width', function(d, i) {
            return d.size * tableW / contentLen;
        })
        .attr('fill', function (d, i) { return sliderGetColor(i); })
        .attr('opacity', TABLE_OPACITY);

    //alert(data[0].objects);
    
    //pans.enter()
    //    .append('g')
    //    .class('panelContent')
    //    .attr('d', function (d, i) { return d; });
    
    //alert('e');

    tablePanel.selectAll('g').remove();

    var infos = pans.each(function (dp, ip) {

        var cx = (tableX + dp.position * tableW / contentLen) + 10;
        var cy = tableY + 10;
        var contPanel = tablePanel.append('g')
                        .attr('transform', 'translate(' + cx + ',' + cy + ')');
        var cw = dp.size * tableW / contentLen - 20;


        var cont = contPanel.selectAll('rect.content')
                    .data(dp.objects)
        cont.enter()
            .append('rect')
            .attr('class', 'content')
            .attr('height', 75)
            .attr('y', function (d, i) {
                return (75 + 6) * i;
            })
            .on('mousemove', function () {
                moveTooltip();
            })
            .on('mouseenter', function (d) {
                showTooltip(d.name);
            })
            .on('mouseout', function (d) {
                hideTooltip();
            })
        cont
            .attr('x', 0)
            .attr('width', cw)
            .attr('fill', d3.rgb(sliderGetColor(ip)).brighter());
        
        cont.exit().remove();
        cont.each(function (d, i) {
            contPanel.append('text')
                .text(d.name)
                //.attr('text-anchor', 'left')
                .attr('pointer-events', 'none')
                .style('font-weight', 'bold')
                .attr({ x: 12, y: 86 * i + 22 });
            contPanel.append('text')
                .text(d.desc)
                .style('font-size', 'small')
                //.attr('text-anchor', 'left')
                .attr('pointer-events', 'none')
                .attr({ x: 24, y: 86 * i + 40 });
        });
    });

    //infos.exit().remove();
    //infos.enter().append('rect')
    //    .attr('class', 'panelData')
    //    .attr('x', 50);
    //.attr('y', function(d, i) {
    //    return i * 50;
    //})

   
}
//function hideTable() {
//    if (!tableShown)
//        EventException();
//    tableShown = false;
//    transitionPanel.selectAll('path')
//        .transition().duration(250)
//        .attr('opacity', 0);

//    tablePanel.selectAll('rect')
//        .transition().duration(250)
//        .attr('opacity', 0)
//        .each('end', function()
//        {
//            tablePanel.selectAll('path').remove();
//            transitionPanel.selectAll('rect').remove();
//        });
//}