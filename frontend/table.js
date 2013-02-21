
var TABLE_BG_OPACITY = 0.15,
    TABLE_TRANSITION_OPACITY = 1,
    TABLE_OPACITY = 1;
    

var tableW = 0,
    tableH = 280,
    tableX,
    tableY;

var tableShown;

var tableContainer;

var transitionGroup;

function setupTable() {
    tableContainer = svg.append('g')
        .attr('id', 'tableGroup')
        //.append('rect')
        //.attr({ x: 0, y: 0, width: tableW, height: tableH });
    transitionGroup = svg.append('g')
        .attr('id', 'transitionGroup');
}

var lineFunction = d3.svg.line()
                         .x(function (d, i) { return d.x; })
                         .y(function (d, i) { return d.y; })

function showTable(data, startX, startY, startW, tX, tY, tw) {
    if (tableShown)
        hideTable();

    //args to vars
    tableW = tw;
    tableX = tX;
    tableY = tY;
    tableShown = true;

    drawTableBg();

    for (var i = 0; i < data.length; i++) {
        var activity = data[i];
        var pts =  [{ x: startX + activity[2] * startW / contentLen, y: startY },
                    //{ x: startX + activity[2] * startW / contentLen, y: startY + (tableY - startY) * 0.2 },
                    { x: startX + activity[2] * startW / contentLen, y: startY + barHeight / 10 },
                    { x: tableX + activity[2] * tableW / contentLen, y: tableY },
                    { x: tableX + (activity[2] + activity[1]) * tableW / contentLen, y: tableY },
                    //{ x: startX + (activity[2] + activity[1]) * startW / contentLen, y: startY + (tableY - startY) * 0.2 },
                    { x: startX + (activity[2] + activity[1]) * startW / contentLen, y: startY + barHeight / 10 },
                    { x: startX + (activity[2] + activity[1]) * startW / contentLen, y: startY }];

        var tmp = transitionGroup.append('path')
                .data(pts)
                .attr("d", lineFunction(pts))
                //.attr('transform', 'translate(' + (w * day[i][2] / totalLen) + ', 0)')
                .attr('fill', function (d) { return sliderGetColor(i); })
                .attr('opacity', TABLE_TRANSITION_OPACITY)

        //    .datum(i)
        //    .attr('transform', 'scale(0, 0)')
        //.transform().duration(500)
        //    .attr('transform', 'scale(1, 1)')

        

        tableContainer.append('rect')
            .attr({ x: tableX + activity[2] * tableW / contentLen, y: tableY - 1, width: activity[1] * tableW / contentLen, height: tableH })
                .attr('fill', function (d) { return sliderGetColor(i); })
                .attr('opacity', TABLE_OPACITY);
        //.transition().duration(250)
        //.attr('height', tableH);
    }
}
function hideTable() {
    if (!tableShown)
        EventException();
    tableShown = false;
    transitionGroup.selectAll('path')
        .transition().duration(250)
        .attr('opacity', 0);

    tableContainer.selectAll('rect')
        .transition().duration(250)
        .attr('opacity', 0)
        .each('end', function()
        {
            tableContainer.selectAll('path').remove();
            transitionGroup.selectAll('rect').remove();
        });
}
function drawTableBg(id) {
    var off = (CONTENT_OFFSET * dayLength);
    var pts = [{ x: dayLength * sliderPos, y: barHeight },
             { x: tableX - off, y: tableY },
             { x: tableX - off, y: tableY + tableH + off },
             { x: tableX + tableW + off, y: tableY + tableH + off },
             { x: tableX + tableW + off, y: tableY },
             { x: dayLength * (sliderPos + 1), y: barHeight }];

    tableContainer.append('path')
            .attr('id', 'menuSelection')
            .data(pts)
            .attr("d", lineFunction(pts))
            //.attr('transform', 'translate(' + (w * day[i][2] / totalLen) + ', 0)')
            //.attr('fill', sliderColor)
            .attr('opacity', TABLE_BG_OPACITY)
}